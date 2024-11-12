# forms.py
from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Tutor, ProgrammingLanguage, SignLanguage, DayAvailability, TimeSlot
import re

class TutorAdminForm(forms.ModelForm):
    """
    Custom form for validating Tutor fields in the admin.
    Ensures that at least one of the many-to-many fields is selected.
    """
    class Meta:
        model = Tutor
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()

        # Get the ManyToMany fields
        programming_languages = cleaned_data.get('programming_languages')
        sign_languages = cleaned_data.get('sign_languages')
        day_availability = cleaned_data.get('day_availability')
        time_availability = cleaned_data.get('time_availability')

        # Custom validation: check if any of the M2M fields are empty
        if not programming_languages:
            raise ValidationError("Please select at least one programming language.")
        if not sign_languages:
            raise ValidationError("Please select at least one sign language.")
        if not day_availability:
            raise ValidationError("Please select at least one day of availability.")
        if not time_availability:
            raise ValidationError("Please select at least one time slot.")

        return cleaned_data

class TutorForm(forms.ModelForm):
    """
    A form for creating and updating Tutor instances.
    This form handles the validation and presentation of fields related to the tutor, including
    programming languages, sign languages, availability, price, and a profile picture.
    """
    programming_languages = forms.ModelMultipleChoiceField(
        queryset=ProgrammingLanguage.objects.all(),
        widget=forms.SelectMultiple(attrs={'size': '5'}),
        required=True,
        error_messages={'required': _("Please select at least one programming language.")}
    )

    sign_languages = forms.ModelMultipleChoiceField(
        queryset=SignLanguage.objects.all(),
        widget=forms.SelectMultiple(attrs={'size': '5'}),
        required=True,
        error_messages={'required': _("Please select at least one sign language.")}
    )

    day_availability = forms.ModelMultipleChoiceField(
        queryset=DayAvailability.objects.all(),
        widget=forms.SelectMultiple(attrs={'size': '5'}),
        required=True,
        error_messages={'required': _("Please select at least one day of availability.")}
    )

    time_availability = forms.ModelMultipleChoiceField(
        queryset=TimeSlot.objects.all(),
        widget=forms.SelectMultiple(attrs={'size': '5'}),
        required=True,
        error_messages={'required': _("Please select at least one time slot.")}
    )

    price = forms.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[
            MinValueValidator(0.00),
            MaxValueValidator(99.99)
        ],
        widget=forms.TextInput(attrs={
            'placeholder': '0.00',
            'class': 'form-control price-input'
        })
    )

    photo = forms.ImageField(required=True, error_messages={'required': _("Please upload a profile picture."), 'invalid': _("Invalid image file.")})

    class Meta:
        """
        The Meta class defines the model and fields that should be used in the form.
        It links this form to the Tutor model and specifies the fields to include.

        The widgets dictionary customises the form fields' HTML output.
        It sets placeholders and CSS classes for the first name, last name, and email input fields.
        """
        model = Tutor
        fields = ['tutor_firstname', 'tutor_lastname', 'tutor_email', 'programming_languages', 'sign_languages', 'day_availability', 'time_availability', 'price', 'photo']
        widgets = {
            'tutor_firstname': forms.TextInput(attrs={
                'placeholder': 'Enter your first name',
                'class': 'form-control'
            }),
            'tutor_lastname': forms.TextInput(attrs={
                'placeholder': 'Enter your last name',
                'class': 'form-control'
            }),
            'tutor_email': forms.EmailInput(attrs={
                'placeholder': 'Enter your email address',
                'class': 'form-control'
            }),
        }

    def __init__(self, *args, **kwargs):
        """
        The constructor method initialises the form and sets the default photo URL if the photo is not uploaded.
        It is called whenever the form is instantiated, either empty or with data.
        """
        super().__init__(*args, **kwargs)
        
        # If the form is invalid, set the default photo URL
        if self.instance and not self.instance.photo:
            self.fields['photo'].initial = 'tutor_images/default.jpg'

    def clean_tutor_firstname(self):
        """
        Validates and cleans the tutor's first name.
        - Strips leading/trailing spaces and replaces multiple spaces with a single space.
        - Validates that the first name contains only letters, spaces, apostrophes, and hyphens.
        - Ensures the first name is not empty and contains at least one letter.
        """
        firstname = self.cleaned_data.get('tutor_firstname')

        # Remove leading/trailing spaces in the output to the DB
        legible_firstname = firstname.strip()

        # Replace multiple spaces with a single space in the output to the DB
        legible_firstname = re.sub(r'\s+', ' ', legible_firstname)

        # Ensure no leading or trailing spaces around hyphens prior to the output to the DB
        legible_firstname = re.sub(r'\s*-\s*', '-', legible_firstname)

        # Check if the first name contains only letters, spaces, apostrophes, and hyphens
        if not re.match("^[A-Za-z\s' -]*$", legible_firstname):
            raise ValidationError("First name must contain only letters, spaces, apostrophes, and hyphens.")

        # Check for empty input after legible first name
        if not legible_firstname:
            raise ValidationError("First name cannot be empty.")

        # Ensure at least one letter is present
        if not re.search("[A-Za-z]", legible_firstname):
            raise ValidationError("First name must contain at least one letter.")

        return legible_firstname  # Return the legible first name

    def clean_tutor_lastname(self):
        """
        Validates and cleans the tutor's last name.
        - Strips leading/trailing spaces and replaces multiple spaces with a single space.
        - Validates that the last name contains only letters, spaces, apostrophes, and hyphens.
        - Ensures the last name is not empty and contains at least one letter.
        """
        lastname = self.cleaned_data.get('tutor_lastname')

        # Remove leading/trailing spaces in the output to the DB
        legible_lastname = lastname.strip()

        # Replace multiple spaces with a single space in the output to the DB
        legible_lastname = re.sub(r'\s+', ' ', legible_lastname)

        # Ensure no leading or trailing spaces around hyphens prior to the output to the DB
        legible_lastname = re.sub(r'\s*-\s*', '-', legible_lastname)

        # Check if the last name contains only letters, spaces, apostrophes, and hyphens
        if not re.match("^[A-Za-z\s' -]*$", legible_lastname):
            raise ValidationError("Last name must contain only letters, spaces, apostrophes, and hyphens.")

        # Check for empty input after legible first name
        if not legible_lastname:
            raise ValidationError("Last name cannot be empty.")

        # Ensure at least one letter is present
        if not re.search("[A-Za-z]", legible_lastname):
            raise ValidationError("Last name must contain at least one letter.")

        return legible_lastname  # Return the legible last name

    def clean_tutor_email(self):
        """
        Validates the tutor's email.
        - Checks if the email is provided and raises a validation error if empty.
        """
        email = self.cleaned_data.get('tutor_email')

        # Check if the email is valid using Django's built-in email validator
        if not email:
            raise ValidationError("Email address cannot be empty.")
        return email  # Return the valid email
