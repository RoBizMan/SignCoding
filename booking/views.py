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
    profile = get_object_or_404(Profile, personal_details=request.user)
    tutor_id = request.session.get('tutor_id')
    if not tutor_id:
        return render(request, 'error.html', {'message': 'No tutor selected. Please select a tutor first.'})
    tutor = get_object_or_404(Tutor, id=tutor_id)

    session_date = None

    if request.method == 'POST':
        session_date_str = request.POST.get('session_date')  # Get the session date string
        selected_time_slots = request.POST.getlist('time_slots')

        # Ensure session_date_str is not empty
        if not session_date_str:
            return render(request, 'error.html', {'message': 'Session date is required.'})

        # Parse the session date string to a datetime object (assuming the format is 'DD-MM-YYYY')
        try:
            session_date = datetime.strptime(session_date_str, '%d-%m-%Y').date()  # Convert to Date
        except ValueError:
            return render(request, 'error.html', {'message': 'Invalid session date format.'})
        
        total_price = len(selected_time_slots) * float(tutor.price)

        booking = Booking(
            user=profile,
            tutor=tutor,
            session_date=session_date,
            total_price=total_price  # Set total price here
        )

        try:
            booking.save()
            for time_slot_id in selected_time_slots:
                time_slot = get_object_or_404(TimeSlot, id=time_slot_id)
                booking.session_time.add(time_slot)

            # Add a success message
            messages.success(request, "Your booking has been successfully created! The booking confirmation has been sent to your email address.")

            # Send confirmation emails
            send_booking_confirmation_email(profile, booking)

            # Redirect to the success page after saving the booking
            return redirect('booking_success')

        except Exception as e:
            print(f"Error saving booking or adding time slots: {e}")
            return render(request, 'error.html', {'message': 'An error occurred while processing your booking.'})

    available_dates = get_available_dates(tutor)

    # Initialize available time slots to all time slots
    available_time_slots = tutor.time_availability.all()

    if session_date:  # Only filter if we have a valid session date
        booked_time_slots = Booking.objects.filter(session_date=session_date, tutor=tutor).values_list('session_time', flat=True)
        
        available_time_slots = available_time_slots.exclude(id__in=booked_time_slots)

    # Get fully booked dates for the next 30 days
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
        'fully_booked_dates': fully_booked_dates,  # Pass this to the template
        'available_time_slots': available_time_slots,
    })


@login_required
def booking_success(request):
    # Get the user's profile
    profile = get_object_or_404(Profile, personal_details=request.user)
    
    # Retrieve the latest booking for this user
    latest_booking = Booking.objects.filter(user=profile).order_by('-booking_date').first()
    
    if latest_booking:
        return render(request, 'booking/booking_success.html', {'booking': latest_booking})
    else:
        return render(request, 'error.html', {'message': 'No booking found.'})


def send_booking_confirmation_email(user_profile, booking):
    subject_template = 'emails/booking_confirmation_email_subject.txt'
    body_template = 'emails/booking_confirmation_email_body.html'

    # Render subject and body from templates
    subject = render_to_string(subject_template, {'booking':booking}).strip()
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