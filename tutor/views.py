from django.shortcuts import render, get_object_or_404
from .models import Tutor, DayAvailability, TimeSlot
from django.core.paginator import Paginator

def tutors(request):
    tutors_list = Tutor.objects.all()

    # Limit pills of sign languages to two plus more in a pill in the frontend view
    for tutor in tutors_list:
        programming_languages = tutor.programming_languages.all()
        sign_languages = tutor.sign_languages.all()
        tutor.remaining_programming_languages = max(0, len(programming_languages) - 4)
        tutor.remaining_sign_languages = max(0, len(sign_languages) - 2)

    # Pagination
    paginator = Paginator(tutors_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'tutor/tutors.html', {'page_obj': page_obj})


def tutor_profile(request, tutor_id):
    # Retrieve the data stored in the database
    tutor = get_object_or_404(Tutor, id=tutor_id)
    days_of_week = DayAvailability.objects.all()
    time_slots = TimeSlot.objects.all()

    context = {
        'tutor': tutor,
        'days_of_week': days_of_week,
        'time_slots': time_slots,
    }
    return render(request, 'tutor/tutors_profile.html', context)
