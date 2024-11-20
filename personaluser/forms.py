from allauth.account.forms import SignupForm
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate
import re


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, required=True, label="First Name")
    last_name = forms.CharField(max_length=30, required=True, label="Last Name")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise ValidationError("A user with this email already exists.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise ValidationError("A user with this username already exists.")
        return username


    def clean_first_name(self):
        """
        Validates and cleans the user's first name.
        - Strips leading/trailing spaces and replaces multiple spaces with a single space.
        - Validates that the first name contains only letters, spaces, apostrophes, and hyphens.
        - Ensures the first name is not empty and contains at least one letter.
        """
        first_name = self.cleaned_data.get('first_name')

        if not first_name:
            raise ValidationError("First name cannot be empty.")

        # Remove leading/trailing spaces in the output to the DB
        legible_first_name = first_name.strip()

        # Replace multiple spaces with a single space in the output to the DB
        legible_first_name = re.sub(r'\s+', ' ', legible_first_name)

        # Ensure no leading or trailing spaces around hyphens prior to the output to the DB
        legible_first_name = re.sub(r'\s*-\s*', '-', legible_first_name)

        # Check if the first name contains only letters, spaces, apostrophes, and hyphens
        if not re.match(r"^[A-Za-z\s' -]*$", legible_first_name):
            raise ValidationError("First name must contain only letters, spaces, apostrophes, and hyphens.")

        # Ensure at least one letter is present
        if not re.search(r"[A-Za-z]", legible_first_name):
            raise ValidationError("First name must contain at least one letter.")

        return legible_first_name

    def clean_last_name(self):
        """
        Validates and cleans the user's last name.
        - Strips leading/trailing spaces and replaces multiple spaces with a single space.
        - Validates that the last name contains only letters, spaces, apostrophes, and hyphens.
        - Ensures the last name is not empty and contains at least one letter.
        """
        last_name = self.cleaned_data.get('last_name')

        if not last_name:
            raise ValidationError("Last name cannot be empty.")

        # Remove leading/trailing spaces in the output to the DB
        legible_last_name = last_name.strip()

        # Replace multiple spaces with a single space in the output to the DB
        legible_last_name = re.sub(r'\s+', ' ', legible_last_name)

        # Ensure no leading or trailing spaces around hyphens prior to the output to the DB
        legible_last_name = re.sub(r'\s*-\s*', '-', legible_last_name)

        # Check if the last name contains only letters, spaces, apostrophes, and hyphens
        if not re.match(r"^[A-Za-z\s' -]*$", legible_last_name):
            raise ValidationError("Last name must contain only letters, spaces, apostrophes, and hyphens.")

        # Ensure at least one letter is present
        if not re.search(r"[A-Za-z]", legible_last_name):
            raise ValidationError("Last name must contain at least one letter.")

        return legible_last_name

    def signup(self, request, user):
        """
        Save the user's first and last names after signup.
        """
        user.first_name = self.cleaned_data.get("first_name")
        user.last_name = self.cleaned_data.get("last_name")
        user.save()
        return user


class EditProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True, label="First Name")
    last_name = forms.CharField(max_length=30, required=True, label="Last Name")

    class Meta:
        model = User
        fields = ['first_name', 'last_name']

    def clean_first_name(self):
        """
        Validates and cleans the user's first name.
        """
        first_name = self.cleaned_data.get('first_name')
        if not first_name:
            raise ValidationError("First name cannot be empty.")
        
        first_name = first_name.strip()
        first_name = re.sub(r'\s+', ' ', first_name)
        first_name = re.sub(r'\s*-\s*', '-', first_name)

        if not re.match(r"^[A-Za-z\s' -]*$", first_name):
            raise ValidationError("First name must contain only letters, spaces, apostrophes, and hyphens.")
        
        if not re.search(r"[A-Za-z]", first_name):
            raise ValidationError("First name must contain at least one letter.")
        
        return first_name

    def clean_last_name(self):
        """
        Validates and cleans the user's last name.
        """
        last_name = self.cleaned_data.get('last_name')
        if not last_name:
            raise ValidationError("Last name cannot be empty.")
        
        last_name = last_name.strip()
        last_name = re.sub(r'\s+', ' ', last_name)
        last_name = re.sub(r'\s*-\s*', '-', last_name)

        if not re.match(r"^[A-Za-z\s' -]*$", last_name):
            raise ValidationError("Last name must contain only letters, spaces, apostrophes, and hyphens.")
        
        if not re.search(r"[A-Za-z]", last_name):
            raise ValidationError("Last name must contain at least one letter.")
        
        return last_name
