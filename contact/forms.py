from django import forms
from .models import Contact
import re
from django.core.exceptions import ValidationError


class ContactForm(forms.ModelForm):
    """
    A form for submitting contact messages.

    This form is based on the Contact model and is used to collect
    user input for contact submissions. It includes fields for the
    user's full name, email address, and message.

    Meta class:
        model (Contact): The model associated with this form.
        fields (list): The fields to include in the form.
        widgets (dict): Custom widgets for specific fields.
        labels (dict): Custom labels for form fields.
    """

    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'message']
        widgets = {
            'message': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Type your message here...'
            }),
        }
        labels = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'message': 'Your Message',
        }

    def clean_full_name(self):
        """
        Validates and cleans the contact's full name.

        Raises:
            ValidationError: If the full name is invalid or empty.

        Returns:
            str: The cleaned full name.
        """
        fullname = self.cleaned_data.get('full_name')

        # Remove leading/trailing spaces in output to DB
        legible_fullname = fullname.strip()

        # Replace multiple spaces with a single space in output to DB
        legible_fullname = re.sub(r'\s+', ' ', legible_fullname)

        # Ensure no leading or trailing spaces around hyphens before output DB
        legible_fullname = re.sub(r'\s*-\s*', '-', legible_fullname)

        # Check if full name contains only valid characters
        if not re.match(r"^[A-Za-z\s' -]*$", legible_fullname):
            raise ValidationError(
                "Full name must contain only letters, \
                spaces, apostrophes, and hyphens."
            )

        # Check for empty input after cleaning
        if not legible_fullname:
            raise ValidationError("Full name cannot be empty.")

        # Ensure at least one letter is present
        if not re.search(r"[A-Za-z]", legible_fullname):
            raise ValidationError(
                "Full name must contain at least one letter."
            )

        return legible_fullname  # Return cleaned full name
