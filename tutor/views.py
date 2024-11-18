from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from .models import Tutor, DayAvailability, TimeSlot
from .forms import TutorForm

def tutors(request):
    """
    Retrieves and displays a paginated list of all tutors.
    
    The view limits the display of programming languages and sign languages for each tutor.
    For programming languages, a maximum of 4 are shown, and for sign languages, a maximum of 2 are shown.
    The remaining count of each is calculated and made available for use in the template.
    
    Pagination is applied to the list of tutors to ensure only 5 tutors are displayed per page.

    Args:
        request: The HTTP request object, typically containing GET or POST data and user session data.

    Returns:
        A rendered page ('tutors.html') with the list of tutors and pagination data.
    """
    tutors_list = Tutor.objects.all().order_by('id')

    # Limit pills of programming languages and sign languages in the frontend view
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
    """
    Displays the detailed profile of a specific tutor.
    
    The view retrieves a tutor by ID and also provides the available days of the week and time slots
    for the tutor's availability.
    
    Args:
        request: The HTTP request object.
        tutor_id: The unique ID of the tutor whose profile is to be displayed.

    Returns:
        A rendered page ('tutors_profile.html') showing the tutor's profile details.
    """
    # Retrieve the data stored in the database
    tutor = get_object_or_404(Tutor, id=tutor_id)
    request.session['tutor_id'] = tutor.id
    days_of_week = DayAvailability.objects.all()
    time_slots = TimeSlot.objects.all()

    context = {
        'tutor': tutor,
        'days_of_week': days_of_week,
        'time_slots': time_slots,
    }
    return render(request, 'tutor/tutors_profile.html', context)


def add_tutor(request):
    """
    Handles the form submission for adding a new tutor to the system.
    
    This view is only accessible to authenticated superusers.
    If the request method is POST, it processes the form data and attempts to save a new tutor.
    If the form is valid, the tutor is saved, a success message is displayed, and the user is redirected
    to the tutors list page.
    
    If the form is not valid, errors are printed for debugging purposes, and the form is redisplayed.
    
    Args:
        request: The HTTP request object containing POST data and user session data.

    Returns:
        A rendered page ('tutors_add.html') containing the tutor form, with possible validation errors.
    """
    if not request.user.is_authenticated or not request.user.is_superuser:
        raise PermissionDenied("You do not have permission to access this page.")

    if request.method == "POST":
        form = TutorForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "Tutor added successfully!")
            return redirect('tutors')
        else:
            print("Form errors:", form.errors)
    else:
        form = TutorForm()

    return render(request, 'tutor/tutors_add.html', {'form': form})

def edit_tutor(request, tutor_id):
    """
    Allows a superuser to edit an existing tutor's profile.
    
    The view is similar to the 'add_tutor' view, but it works on an existing tutor record.
    If the tutor exists, it pre-populates the form with the tutor's current data and allows the user
    to make changes. If the form is valid, it saves the changes to the tutor's profile.
    
    Args:
        request: The HTTP request object containing the data submitted via the form.
        tutor_id: The unique ID of the tutor whose profile is to be edited.

    Returns:
        A rendered page ('tutors_edit.html') with the tutor's data pre-filled in the form.
        If successful, it redirects to the tutor's profile page or list of tutors.
    """
    tutor = get_object_or_404(Tutor, id=tutor_id)

    if not request.user.is_authenticated or not request.user.is_superuser:
        raise PermissionDenied("You do not have permission to access this page.")

    if request.method == "POST":
        form = TutorForm(request.POST, request.FILES, instance=tutor)

        if form.is_valid():
            form.save()
            messages.success(request, "Tutor profile updated successfully!")
            return redirect('tutor_profile', tutor_id=tutor.id)
        else:
            print("Form errors:", form.errors)
    else:
        form = TutorForm(instance=tutor)

    return render(request, 'tutor/tutors_edit.html', {'form': form, 'tutor': tutor})

def delete_tutor(request, tutor_id):
    """
    Allows a superuser to delete an existing tutor's profile.

    If the tutor exists and the user is a superuser, it removes the tutor from the database.
    Upon successful deletion, redirects to the tutors list page with a success message.

    Args:
        request: The HTTP request object containing the user and session information.
        tutor_id: The unique ID of the tutor to be deleted.

    Returns:
        A redirect to the list of tutors with a success message.
    """
    if not request.user.is_authenticated or not request.user.is_superuser:
        raise PermissionDenied("You do not have permission to delete this profile.")
    
    tutor = get_object_or_404(Tutor, id=tutor_id)
    tutor.delete()
    messages.success(request, "Tutor profile deleted successfully.")
    return redirect('tutors')
