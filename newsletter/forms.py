# newsletter/forms.py
from django import forms


class NewsletterSubscriptionForm(forms.Form):
    """
    A form for subscribing to the newsletter.

    This form collects the user's email address for newsletter
    subscriptions. It ensures that the email provided is valid
    and required.

    Attributes:
        email (EmailField): The email address of the user, which is
                            required for subscription.
    """

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'})
    )
