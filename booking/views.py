from django.shortcuts import render, get_object_or_404
from tutor.models import Tutor, TimeSlot
from personaluser.models import Profile
from booking.models import Booking
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.http import JsonResponse

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

        except Exception as e:
            print(f"Error saving booking or adding time slots: {e}")

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