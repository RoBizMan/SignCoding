from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Type your message here...'}),
        }
        labels = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'message': 'Your Message',
        }
