# newsletter/forms.py
from django import forms

class NewsletterSubscriptionForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))
