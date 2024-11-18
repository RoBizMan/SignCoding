from django.shortcuts import render, get_object_or_404
from tutor.models import Tutor
from personaluser.models import Profile
from booking.models import Booking
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError

@login_required
def booking_create(request):
    """
    View to create a new booking for a tutor.
    The tutor's availability and session times are displayed.
    """
    profile = get_object_or_404(Profile, personal_details=request.user)
    tutor_id = request.session.get('tutor_id')
    
    if not tutor_id:
        return render(request, 'error.html', {'message': 'No tutor selected for booking.'})
    
    tutor = get_object_or_404(Tutor, id=tutor_id)

    # For GET requests, render the booking page
    return render(request, 'booking/booking_create.html', {'tutor': tutor, 'profile': profile, 'form': form})
