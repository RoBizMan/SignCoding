from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from .models import Profile
from .forms import EditProfileForm

@login_required
def user_profile(request):
    # Get the profile associated with the logged-in user
    profile = get_object_or_404(Profile, personal_details=request.user)

    # Check if the accessed profile belongs to the logged-in user
    if request.user != profile.personal_details:
        raise PermissionDenied("You do not have permission to access this page.")

    return render(request, 'personaluser/my_profile.html', {'profile': profile})


@login_required
def edit_profile(request):
    # Get the profile associated with the logged-in user
    profile = get_object_or_404(Profile, personal_details=request.user)

    # Ensure that the logged-in user is trying to edit their own profile
    if request.user != profile.personal_details:
        raise PermissionDenied("You do not have permission to edit this profile.")

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated successfully.")
            return redirect('user_profile')  # Redirect to the user's profile page
    else:
        form = EditProfileForm(instance=request.user)

    return render(request, 'personaluser/edit_profile.html', {'form': form})


@login_required
def delete_account(request):
    # Get the profile associated with the logged-in user
    profile = get_object_or_404(Profile, personal_details=request.user)

    # Ensure that the logged-in user is trying to delete their own account
    if request.user != profile.personal_details:
        raise PermissionDenied("You do not have permission to delete this account.")

    if request.method == "POST":
        # Delete the user's profile and account
        user = request.user
        user.delete()  # This deletes the user and associated profile

        messages.success(request, "Your account has been deleted successfully.")

        # Redirect to the home page or any other page after deletion
        return redirect('home')  # Adjust this to the correct redirect URL

    return redirect('user_profile')
