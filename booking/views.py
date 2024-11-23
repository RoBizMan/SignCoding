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
from django.db import transaction
from decimal import Decimal
from django.views.decorators.csrf import csrf_protect

stripe.api_key = settings.STRIPE_SECRET_KEY

def get_available_dates(tutor):
    """
    Generate a list of available dates for the given tutor based on their day availability
    for the next 30 days.
    """
    today = datetime.today()
    available_dates = []

    # Get a set of available weekday indices from tutor's day availability
    available_weekdays = {day.name: day.order for day in tutor.day_availability.all()}

    # Get the next 30 days
    for i in range(30):
        current_day = today + timedelta(days=i)
        # Check if the current day's weekday is in the set of available weekdays
        if current_day.strftime('%A') in available_weekdays:
            # Check if all time slots are booked for this date
            total_time_slots = tutor.time_availability.count()
            booked_time_slots_count = Booking.objects.filter(session_date=current_day.date(), tutor=tutor).count()
            
            # If not all time slots are booked, add this date to available dates
            if booked_time_slots_count < total_time_slots:
                available_dates.append(current_day.strftime('%d-%m-%Y'))  # Format as DD-MM-YYYY

    return available_dates


@login_required
def get_available_time_slots(request):
    if request.method == "GET":
        tutor_id = request.GET.get('tutor_id')
        session_date_str = request.GET.get('session_date')

        if not tutor_id or not session_date_str:
            return JsonResponse({'error': 'Invalid parameters'}, status=400)

        tutor = get_object_or_404(Tutor, id=tutor_id)
        
        try:
            session_date = datetime.strptime(session_date_str, '%d-%m-%Y').date()
            booked_time_slots = Booking.objects.filter(session_date=session_date, tutor=tutor).values_list('session_time', flat=True)
            available_time_slots = tutor.time_availability.exclude(id__in=booked_time_slots)

            data = [{'id': ts.id, 'name': str(ts)} for ts in available_time_slots]  # Prepare data for response
            return JsonResponse(data, safe=False)
        
        except ValueError:
            return JsonResponse({'error': 'Invalid date format'}, status=400)


@login_required
def booking_create(request):
    """Handles booking creation and Stripe payment integration."""
    profile = get_object_or_404(Profile, personal_details=request.user)
    tutor_id = request.session.get('tutor_id')
    
    if not tutor_id:
        return render(request, 'error.html', {'message': 'No tutor selected. Please select a tutor first.'})
    
    tutor = get_object_or_404(Tutor, id=tutor_id)
    session_date = None

    if request.method == 'POST':
        session_date_str = request.POST.get('session_date')  # Get session date
        selected_time_slots = request.POST.getlist('time_slots')
        stripe_pid = request.POST.get('stripe_pid')  # Stripe Payment Intent ID

        if not session_date_str:
            return render(request, 'error.html', {'message': 'Session date is required.'})

        try:
            session_date = datetime.strptime(session_date_str, '%d-%m-%Y').date()
        except ValueError:
            return render(request, 'error.html', {'message': 'Invalid session date format.'})

        if not selected_time_slots:
            return render(request, 'error.html', {'message': 'Please select at least one time slot.'})

        # Calculate total price
        total_price = len(selected_time_slots) * float(tutor.price)

        # Create a provisional booking
        booking = Booking(
            user=profile,
            tutor=tutor,
            session_date=session_date,
            total_price=total_price,
            stripe_pid=stripe_pid,  # Save the Stripe Payment Intent ID
        )

        try:
            booking.save()
            for time_slot_id in selected_time_slots:
                time_slot = get_object_or_404(TimeSlot, id=time_slot_id)
                booking.session_time.add(time_slot)

            messages.success(request, "Your booking has been successfully booked!")

            return redirect('booking_success', booking_id=booking.id)
        except Exception as e:
            print(f"Error saving booking: {e}")
            return render(request, 'error.html', {'message': 'An error occurred while processing your booking.'})

    available_dates = get_available_dates(tutor)
    available_time_slots = tutor.time_availability.all()

    if session_date:
        booked_time_slots = Booking.objects.filter(session_date=session_date, tutor=tutor).values_list('session_time', flat=True)
        available_time_slots = available_time_slots.exclude(id__in=booked_time_slots)

    today = datetime.today()
    fully_booked_dates = []

    for i in range(30):
        current_day = today + timedelta(days=i)
        total_time_slots = tutor.time_availability.count()
        booked_time_slots_count = Booking.objects.filter(session_date=current_day.date(), tutor=tutor).count()

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
    if request.method == "POST":
        total_price = request.POST.get('total_price')
        tutor_id = request.POST.get('tutor')  # Tutor ID sent from the frontend

        # Get the profile of the currently logged-in user
        user_profile = request.user.profile  # Profile model linked to the logged-in user

        # Ensure that the tutor ID is sent in the request
        try:
            tutor = Tutor.objects.get(id=tutor_id)  # Fetch the tutor based on ID from the request
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
                    'user': user_profile.personal_details.username,  # Access username via personal_details
                    'tutor_firstname': tutor_first_name,  # Access first name from Tutor model
                    'tutor_lastname': tutor_last_name,  # Access last name from Tutor model
                    'tutor_email': tutor_email,
                }
            )
            return JsonResponse({'client_secret': payment_intent['client_secret']})
        except Exception as e:
            print(f"Error creating Payment Intent: {e}")
            return JsonResponse({'error': str(e)}, status=400)


@login_required
def booking_success(request, booking_id):
    """
    Displays booking confirmation details.
    """
    # Retrieve the booking
    booking = get_object_or_404(Booking, id=booking_id)

    # Ensure the booking belongs to the logged-in user
    if booking.user != request.user.profile:
        return render(request, 'error.html', {'message': 'Booking not found.'})

    # Check payment status
    if booking.payment_status == 'paid':
        messages.success(request, "Your payment was successful! Details of your booking are below.")
    elif booking.payment_status == 'failed':
        messages.error(request, "Payment failed. Please retry or contact support.")

    return render(request, 'booking/booking_success.html', {'booking': booking})


def send_booking_confirmation_email(user_profile, booking):
    subject_template = 'emails/booking_confirmation_email_subject.txt'
    body_template = 'emails/booking_confirmation_email_body.html'

    # Render subject and body from templates
    subject = render_to_string(subject_template, {'booking': booking}).strip()
    context = {
        'user': user_profile,
        'booking': booking,
    }
    
    # Render HTML content from body template
    html_content = render_to_string(body_template, context)

    # Create email message for user
    user_email = user_profile.personal_details.email
    email_to_user = EmailMultiAlternatives(subject, '', 'arsenalpure95@gmail.com', [user_email])
    email_to_user.attach_alternative(html_content, "text/html")
    
    # Send email to user
    email_to_user.send()

    # Create email message for tutor
    tutor_email = booking.tutor.tutor_email
    email_to_tutor = EmailMultiAlternatives(subject, '', 'arsenalpure95@gmail.com', [tutor_email])
    email_to_tutor.attach_alternative(html_content, "text/html")
    
    # Send email to tutor
    email_to_tutor.send()
