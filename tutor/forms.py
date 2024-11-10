# forms.py
from django import forms
from django.core.exceptions import ValidationError
from .models import Tutor

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
