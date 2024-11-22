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
    """ Handles booking creation and integrates Stripe payment validation. """
    profile = get_object_or_404(Profile, personal_details=request.user)
    tutor_id = request.session.get('tutor_id')
    
    if not tutor_id:
        return render(request, 'error.html', {'message': 'No tutor selected. Please select a tutor first.'})
    
    tutor = get_object_or_404(Tutor, id=tutor_id)
    session_date = None

    if request.method == 'POST':
        session_date_str = request.POST.get('session_date')  # Get the session date string
        selected_time_slots = request.POST.getlist('time_slots')
        stripe_pid = request.POST.get('stripe_pid')  # Get Stripe Payment Intent ID from the form

        # Ensure session_date_str is not empty
        if not session_date_str:
            return render(request, 'error.html', {'message': 'Session date is required.'})

        # Parse the session date string to a datetime object (assuming the format is 'DD-MM-YYYY')
        try:
            session_date = datetime.strptime(session_date_str, '%d-%m-%Y').date()  # Convert to Date
        except ValueError:
            return render(request, 'error.html', {'message': 'Invalid session date format.'})

        # Check if any time slots were selected
        if not selected_time_slots:
            return render(request, 'error.html', {'message': 'Please select at least one time slot.'})

        total_price = len(selected_time_slots) * float(tutor.price)  # Calculate total price in euros
        total_price_cents = int(total_price * 100)  # Convert to cents for Stripe

        # Validate the payment with Stripe
        try:
            payment_intent = stripe.PaymentIntent.retrieve(stripe_pid)
            amount_received = payment_intent['amount_received']  # Amount received in cents
            
            # Debugging logs for comparison
            print(f"Expected amount (cents): {total_price_cents}, Amount received (cents): {amount_received}")

            if amount_received != total_price_cents:  # Compare amounts in cents
                return render(request, 'error.html', {'message': 'Payment amount does not match.'})
        except stripe.error.StripeError as e:
            return render(request, 'error.html', {'message': f'Stripe error: {str(e)}'})

        # Create the booking
        booking = Booking(
            user=profile,
            tutor=tutor,
            session_date=session_date,
            total_price=total_price,  # Store total price in euros
            stripe_pid=stripe_pid,  # Save the Stripe Payment Intent ID
        )

        try:
            booking.save()
            for time_slot_id in selected_time_slots:
                time_slot = get_object_or_404(TimeSlot, id=time_slot_id)
                booking.session_time.add(time_slot)

            messages.success(request, "Your booking has been successfully created! A confirmation email has been sent.")
            
            send_booking_confirmation_email(profile, booking)

            return redirect('booking_success', booking_id=booking.id)

        except Exception as e:
            print(f"Error saving booking or adding time slots: {e}")
            return render(request, 'error.html', {'message': 'An error occurred while processing your booking.'})

    available_dates = get_available_dates(tutor)

    available_time_slots = tutor.time_availability.all()

    if session_date:  # Only filter if we have a valid session date
        booked_time_slots = Booking.objects.filter(session_date=session_date, tutor=tutor).values_list('session_time', flat=True)
        available_time_slots = available_time_slots.exclude(id__in=booked_time_slots)

    today = datetime.today()  # Define today here
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


@csrf_protect  # Ensure CSRF protection is enabled
def create_payment_intent(request):
    if request.method == "POST":
        total_price = request.POST.get('total_price')
        
        try:
            # Create a Payment Intent with Stripe
            payment_intent = stripe.PaymentIntent.create(
                amount=int(float(total_price) * 100),  # Convert to cents
                currency='eur',
                # Optionally add metadata or other parameters here
            )
            return JsonResponse({'client_secret': payment_intent['client_secret']})
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)


@login_required
def booking_success(request, booking_id):
    """
    Displays booking confirmation details.
    """
    # Get the specific booking for this user
    booking = get_object_or_404(Booking, id=booking_id)

    # Ensure the booking belongs to the logged-in user
    if booking.user != request.user.profile:
        return render(request, 'error.html', {'message': 'Booking not found.'})

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
