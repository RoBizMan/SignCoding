from django.shortcuts import render

# Create your views here.


def tutors(request):
    return render(request, 'tutor/tutors.html')
