from django.shortcuts import render
from .models import Tutor

# Create your views here.
def tutors(request):
    tutors = Tutor.objects.all()

    # Limit pills of sign languages to two plus more in a pill in the frontend view
    for tutor in tutors:
        programming_languages = tutor.programming_languages.all()
        sign_languages = tutor.sign_languages.all()
        tutor.remaining_programming_languages = max(0, len(programming_languages) - 4)
        tutor.remaining_sign_languages = max(0, len(sign_languages) - 2)

    return render(request, 'tutor/tutors.html', {'tutors': tutors})
