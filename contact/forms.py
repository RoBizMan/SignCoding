from django import forms
from .models import Contact


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
