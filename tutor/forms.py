from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import (
    Tutor, ProgrammingLanguage, SignLanguage, DayAvailability, TimeSlot
)
from cloudinary.forms import CloudinaryFileField
import re


class TutorAdminForm(forms.ModelForm):
    """
    Custom form for validating Tutor fields in the admin.

    This form ensures that at least one of the many-to-many fields
    (programming languages, sign languages, day availability, and
    time availability) is selected before a tutor can be saved.

    Attributes:
        model (Type[Tutor]): The model associated with this form.
        fields (list): All fields from the Tutor model.
    """

    class Meta:
        model = Tutor
        fields = '__all__'

    def clean(self):
        """
        Custom validation to ensure that required Many-to-Many fields
        are selected.

        Raises:
            ValidationError: If any of the required Many-to-Many fields
            are empty.

        Returns:
            dict: Cleaned data from the form.
        """
        cleaned_data = super().clean()

        # Get the ManyToMany fields
        programming_languages = cleaned_data.get('programming_languages')
        sign_languages = cleaned_data.get('sign_languages')
        day_availability = cleaned_data.get('day_availability')
        time_availability = cleaned_data.get('time_availability')

        # Custom validation: check if any of the M2M fields are empty
        if not programming_languages:
            raise ValidationError(
                "Please select at least one programming language."
            )
        if not sign_languages:
            raise ValidationError(
                "Please select at least one sign language."
            )
        if not day_availability:
            raise ValidationError(
                "Please select at least one day of availability."
            )
        if not time_availability:
            raise ValidationError("Please select at least one time slot.")

        return cleaned_data


class TutorForm(forms.ModelForm):
    """
    A form for creating and updating Tutor instances.

    This form handles the validation and presentation of fields related
    to the tutor, including programming languages, sign languages,
    availability, price, and a profile picture.

    Attributes:
        programming_languages (ModelMultipleChoiceField): The programming
            languages that the tutor can teach.
        sign_languages (ModelMultipleChoiceField): The sign languages that
            the tutor can teach.
        day_availability (ModelMultipleChoiceField): The days of the week
            when the tutor is available.
        time_availability (ModelMultipleChoiceField): The time slots when
            the tutor is available.
        price (DecimalField): The hourly rate of the tutor.
        photo (CloudinaryFileField): The profile picture of the tutor.
    """

    programming_languages = forms.ModelMultipleChoiceField(
        queryset=ProgrammingLanguage.objects.all(),
        widget=forms.SelectMultiple(attrs={'size': '5'}),
        required=True,
        error_messages={
            'required': _("Please select at least one programming language.")
        }
    )

    sign_languages = forms.ModelMultipleChoiceField(
        queryset=SignLanguage.objects.all(),
        widget=forms.SelectMultiple(attrs={'size': '5'}),
        required=True,
        error_messages={
            'required': _("Please select at least one sign language.")
        }
    )

    day_availability = forms.ModelMultipleChoiceField(
        queryset=DayAvailability.objects.all(),
        widget=forms.SelectMultiple(attrs={'size': '5'}),
        required=True,
        error_messages={
            'required': _("Please select at least one day of availability.")
        }
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

    photo = CloudinaryFileField(
        required=True,
        error_messages={
            'required': _("Please upload a profile picture."),
            'invalid': _("Invalid image file.")
        }
    )

    class Meta:
        model = Tutor
        fields = [
            'tutor_firstname', 'tutor_lastname', 'tutor_email',
            'programming_languages', 'sign_languages',
            'day_availability', 'time_availability', 'price', 'photo'
        ]
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
        Initializes the form and sets a default photo URL if not uploaded.

        Args:
            args: Positional arguments for form initialization.
            kwargs: Keyword arguments for form initialization.
        """
        super().__init__(*args, **kwargs)

        # If the form is invalid, set the default photo URL
        if self.instance and not self.instance.photo:
            self.fields['photo'].initial = 'tutor_images/default.jpg'

    def clean_tutor_firstname(self):
        """
        Validates and cleans the tutor's first name.

        Raises:
            ValidationError: If the first name is invalid or empty.

        Returns:
            str: The cleaned first name.
        """
        firstname = self.cleaned_data.get('tutor_firstname')

        # Remove leading/trailing spaces in the output to the DB
        legible_firstname = firstname.strip()

        # Replace multiple spaces with a single space in the output to the DB
        legible_firstname = re.sub(r'\s+', ' ', legible_firstname)

        # Ensure no leading or trailing spaces around hyphens before output DB
        legible_firstname = re.sub(r'\s*-\s*', '-', legible_firstname)

        # Check if first name contains only valid characters
        if not re.match(r"^[A-Za-z\s' -]*$", legible_firstname):
            raise ValidationError(
                "First name must contain only letters, \
                spaces, apostrophes, and hyphens."
            )

        # Check for empty input after cleaning
        if not legible_firstname:
            raise ValidationError("First name cannot be empty.")

        # Ensure at least one letter is present
        if not re.search(r"[A-Za-z]", legible_firstname):
            raise ValidationError(
                "First name must contain at least one letter."
            )

        return legible_firstname  # Return cleaned first name

    def clean_tutor_lastname(self):
        """
        Validates and cleans the tutor's last name.

        Raises:
            ValidationError: If the last name is invalid or empty.

        Returns:
            str: The cleaned last name.
        """
        lastname = self.cleaned_data.get('tutor_lastname')

        # Remove leading/trailing spaces in output to DB
        legible_lastname = lastname.strip()

        # Replace multiple spaces with a single space in output to DB
        legible_lastname = re.sub(r'\s+', ' ', legible_lastname)

        # Ensure no leading or trailing spaces around hyphens before output DB
        legible_lastname = re.sub(r'\s*-\s*', '-', legible_lastname)

        # Check if last name contains only valid characters
        if not re.match(r"^[A-Za-z\s' -]*$", legible_lastname):
            raise ValidationError(
                "Last name must contain only letters, \
                spaces, apostrophes, and hyphens."
            )

        # Check for empty input after cleaning
        if not legible_lastname:
            raise ValidationError("Last name cannot be empty.")

        # Ensure at least one letter is present
        if not re.search(r"[A-Za-z]", legible_lastname):
            raise ValidationError(
                "Last name must contain at least one letter."
            )

        return legible_lastname  # Return cleaned last name

    def clean_tutor_email(self):
        """
        Validates the tutor's email.

        Raises:
            ValidationError: If email is empty or invalid.

        Returns:
            str: The cleaned email address.
        """
        email = self.cleaned_data.get('tutor_email')

        # Check if email is valid using Django's built-in email validator
        if not email:
            raise ValidationError("Email address cannot be empty.")
        return email  # Return valid email address
