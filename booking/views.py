from django.shortcuts import render, get_object_or_404, redirect
from tutor.models import Tutor, TimeSlot
from personaluser.models import Profile
from booking.models import Booking
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.http import JsonResponse
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
import stripe
from django.conf import settings
from django.db import transaction, models
from django.db.models import Count
from decimal import Decimal
from django.views.decorators.csrf import csrf_protect

# Set the Stripe API key from settings
stripe.api_key = settings.STRIPE_SECRET_KEY


def get_available_dates(tutor):
    """
    Generate a list of available dates for the given tutor based on their
    day availability for the next 30 days. Today's date is excluded, and
    users must book at least 24 hours in advance.

    Args:
        tutor (Tutor): The tutor for whom to check availability.

    Returns:
        List[str]: A list of available dates in 'dd-mm-yyyy' format.
    """
    today = datetime.today()
    available_dates = []

    # Get a set of available weekday indices from tutor's day availability
    available_weekdays = {
        day.name: day.order for day in
        tutor.day_availability.all()
    }

    # Get the next 30 days
    for i in range(30):
        current_day = today + timedelta(days=i)

        # Skip today entirely
        if current_day.date() == today.date():
            continue

        # Check if the current day's weekday is in set of available weekdays
        if current_day.strftime('%A') in available_weekdays:
            # Check the total time slots for this day
            total_time_slots = tutor.time_availability.count()

            # Count how many unique time slots are booked for this day
            booked_time_slots_count = Booking.objects.filter(
                session_date=current_day.date(),
                tutor=tutor
            ).aggregate(
                total_booked=Count('session_time')
            )['total_booked'] or 0

            # If the number of booked time slots is equal to or greater than
            # the total time slots, it's fully booked
            if booked_time_slots_count >= total_time_slots:
                continue  # Skip adding this date as it's fully booked

            # If there are available time slots, add date to available dates
            available_dates.append(current_day.strftime('%d-%m-%Y'))

    # Filter out dates that are less than 24 hours from now
    available_dates = [
        date for date in available_dates if (
            datetime.strptime(date, '%d-%m-%Y') - today
        ).days >= 1
    ]

    return available_dates


@login_required
def get_available_time_slots(request):
    """
    Retrieves available time slots for a specific tutor and session date.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response containing available time slots or an
                        error message.
    """
    if request.method == "GET":
        tutor_id = request.GET.get('tutor_id')
        session_date_str = request.GET.get('session_date')

        if not tutor_id or not session_date_str:
            return JsonResponse({'error': 'Invalid parameters'}, status=400)

        tutor = get_object_or_404(Tutor, id=tutor_id)

        try:
            session_date = datetime.strptime(
                session_date_str, '%d-%m-%Y'
            ).date()
            booked_time_slots = Booking.objects.filter(
                session_date=session_date,
                tutor=tutor).values_list('session_time', flat=True)
            available_time_slots = tutor.time_availability.exclude(
                id__in=booked_time_slots)

            data = [{'id': ts.id, 'name': str(ts)} for ts in
                    available_time_slots]  # Prepare data for response

            return JsonResponse(data, safe=False)

        except ValueError:
            return JsonResponse({'error': 'Invalid date format'}, status=400)


@login_required
def booking_create(request):
    """
    Handles booking creation and Stripe payment integration.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Renders the booking creation page or redirects to the
                        success page upon successful booking.
    """
    profile = get_object_or_404(Profile, personal_details=request.user)
    tutor_id = request.session.get('tutor_id')

    if not tutor_id:
        return render(request, 'error.html', {
            'message': 'No tutor selected. Please select a tutor first.'
        })

    tutor = get_object_or_404(Tutor, id=tutor_id)

    session_date = None

    if request.method == 'POST':
        session_date_str = request.POST.get('session_date')  # Get session date
        selected_time_slots = request.POST.getlist('time_slots')
        stripe_pid = request.POST.get('stripe_pid')  # Stripe Payment Intent ID

        if not session_date_str:
            return render(request, 'error.html', {
                'message': 'Session date is required.'
            })

        try:
            session_date = datetime.strptime(
                session_date_str, '%d-%m-%Y'
            ).date()
        except ValueError:
            return render(request, 'error.html', {
                'message': 'Invalid session date format.'
            })

        if not selected_time_slots:
            return render(request, 'error.html', {
                'message': 'Please select at least one time slot.'
            })

        # Calculate total price
        total_price = len(selected_time_slots) * float(tutor.price)

        try:
            # Confirm the payment status using Stripe API
            payment_intent = stripe.PaymentIntent.retrieve(stripe_pid)

            if payment_intent['status'] != 'succeeded':
                messages.error(request, "Payment failed. Please try again.")
                return render(request, 'error.html', {
                    'message':
                        'Payment was not successful. \
                        Booking cannot be confirmed.'
                })

            # Create a provisional booking only if payment is successful
            booking = Booking(
                user=profile,
                tutor=tutor,
                session_date=session_date,
                total_price=total_price,
                stripe_pid=stripe_pid,  # Save the Stripe Payment Intent ID
                payment_status='paid'  # Set the payment status to paid
            )

            booking.user_fullname = f"{profile.personal_firstname} \
            {profile.personal_lastname}"
            booking.user_email = profile.personal_details.email

            booking.tutor_fullname = f"{tutor.tutor_firstname} \
            {tutor.tutor_lastname}"
            booking.tutor_email = tutor.tutor_email

            booking.save()  # Save booking first

            for time_slot_id in selected_time_slots:
                time_slot = get_object_or_404(TimeSlot, id=time_slot_id)
                # Associate time slot with the booking
                booking.session_time.add(time_slot)

            messages.success(
                request, "Your booking has been successfully booked!"
            )

            # Recalculate availability after saving booking
            available_dates = get_available_dates(tutor)

            fully_booked_dates = []  # Clear previous fully booked dates

            today = datetime.today()

            # Check again for fully booked dates based on all bookings after
            # new booking is saved.
            for i in range(1, 30):  # Start from 1 to skip today
                current_day = today + timedelta(days=i)
                total_time_slots = tutor.time_availability.count()

                booked_time_slots_count = Booking.objects.filter(
                    session_date=current_day.date(),
                    tutor=tutor
                ).aggregate(
                    total_booked=Count('session_time')
                )['total_booked'] or 0

                if booked_time_slots_count >= total_time_slots:
                    fully_booked_dates.append(current_day.strftime('%d-%m-%Y'))

            send_booking_confirmation_email(profile, booking)

            return redirect('booking_success', booking_id=booking.id)

        except Exception as e:
            print(f"Error saving booking: {e}")
            return render(request, 'error.html', {
                'message': 'An error occurred while processing your booking.'
            })

    available_dates = get_available_dates(tutor)
    available_time_slots = tutor.time_availability.all()

    if session_date:
        booked_time_slots = Booking.objects.filter(
            session_date=session_date, tutor=tutor
        ).values_list('session_time', flat=True)

        available_time_slots = available_time_slots.exclude(
                                                    id__in=booked_time_slots
                                                    )

    today = datetime.today()
    fully_booked_dates = []

    for i in range(1, 30):  # Start from 1 to skip today
        current_day = today + timedelta(days=i)
        total_time_slots = tutor.time_availability.count()

        booked_time_slots_count = Booking.objects.filter(
            session_date=current_day.date(), tutor=tutor
        ).aggregate(total_booked=Count('session_time'))['total_booked'] or 0

        if booked_time_slots_count >= total_time_slots:
            fully_booked_dates.append(current_day.strftime('%d-%m-%Y'))

    return render(request, 'booking/booking_create.html', {
        'tutor': tutor,
        'profile': profile,
        'available_dates': available_dates,
        'fully_booked_dates': fully_booked_dates,
        'available_time_slots': available_time_slots,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
    })


@csrf_protect
def create_payment_intent(request):
    """
    Creates a Stripe Payment Intent based on the total price and selected
    tutor.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response containing the client secret of the
                        created Payment Intent or an error message.
    """

    if request.method == "POST":
        total_price = request.POST.get('total_price')

        tutor_id = request.POST.get('tutor')  # Tutor ID sent from the frontend

        # Get the profile of the currently logged-in user
        user_profile = request.user.profile

        try:
            # Fetch the tutor based on ID from the request
            tutor = Tutor.objects.get(id=tutor_id)

        except Tutor.DoesNotExist:
            return JsonResponse({'error': 'Tutor not found'}, status=400)

        try:
            # Access tutor's first name and last name from the Tutor model
            tutor_first_name = tutor.tutor_firstname
            tutor_last_name = tutor.tutor_lastname
            tutor_email = tutor.tutor_email

            # Create a Payment Intent with Stripe
            payment_intent = stripe.PaymentIntent.create(
                amount=int(float(total_price) * 100),  # Convert to cents
                currency='eur',
                metadata={
                    'user': user_profile.personal_details.username,
                    'tutor_firstname': tutor_first_name,
                    'tutor_lastname': tutor_last_name,
                    'tutor_email': tutor_email,
                }
            )

            return JsonResponse(
                {'client_secret': payment_intent['client_secret']}
            )

        except Exception as e:
            print(f"Error creating Payment Intent: {e}")

            return JsonResponse({'error': str(e)}, status=400)


@login_required
def booking_success(request, booking_id):
    """
    Displays booking confirmation details.

    Args:
        request (HttpRequest): The HTTP request object.
        booking_id (int): The ID of the completed booking.

    Returns:
        HttpResponse: Renders the success page with booking details or an
                        error message.
    """

    # Retrieve the booking by ID.
    booking = get_object_or_404(Booking, id=booking_id)

    # Ensure the booking belongs to the logged-in user.
    if booking.user != request.user.profile:
        return render(request, 'error.html', {'message': 'Booking not found.'})

    # Check payment status and set appropriate message.
    if booking.payment_status == 'paid':
        messages.success(
            request, "Your payment was successful! Details of your \
            booking are below."
        )

    elif booking.payment_status == 'failed':
        messages.error(
            request, "Payment failed. Please retry or contact support."
        )

    return render(
        request, 'booking/booking_success.html', {'booking': booking}
    )


def send_booking_confirmation_email(user_profile, booking):
    """
    Sends a confirmation email to both user and tutor after successful
    booking.

    Args:
        user_profile (Profile): The profile of the user who made the
                                booking.
        booking (Booking): The Booking instance containing details of
                            the reservation.
    """

    subject_template = 'emails/booking_confirmation_email_subject.txt'
    body_template = 'emails/booking_confirmation_email_body.html'

    # Render subject and body from templates.
    subject = render_to_string(subject_template, {'booking': booking}).strip()
    context = {
        'user': user_profile,
        'booking': booking,
    }

    # Render HTML content from body template.
    html_content = render_to_string(body_template, context)

    # Create email message for user.
    user_email = user_profile.personal_details.email

    email_to_user = EmailMultiAlternatives(
        subject='', body='', from_email='arsenalpure95@gmail.com',
        to=[user_email]
    )

    email_to_user.attach_alternative(html_content, "text/html")

    # Send email to user.
    email_to_user.send()

    # Create email message for tutor.
    tutor_email = booking.tutor.tutor_email

    email_to_tutor = EmailMultiAlternatives(
        subject='', body='', from_email='arsenalpure95@gmail.com',
        to=[tutor_email]
    )

    email_to_tutor.attach_alternative(html_content, "text/html")

    # Send email to tutor.
    email_to_tutor.send()
