from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.contrib import messages
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from .models import NewsletterSubscription


def send_newsletter_confirmation_email(email):
    """
    Sends a confirmation email to the user after a successful
    newsletter subscription.

    Args:
        email (str): The email address of the subscriber.
    """
    # Render email subject and body from templates
    subject = render_to_string(
        'emails/newsletter_confirmation_email_subject.txt', {'email': email}
    )
    body = render_to_string(
        'emails/newsletter_confirmation_email_body.html', {'email': email}
    )

    # Send email using Django's send_mail function
    send_mail(
        subject.strip(),  # Subject line
        body.strip(),     # Body of the email (ensure it’s not None or empty)
        settings.DEFAULT_FROM_EMAIL,  # From email
        [email],          # To email (make sure it's list containing email)
        html_message=body  # HTML content
    )


def subscribe_newsletter(request):
    """
    Handles the subscription process for the newsletter.

    Validates the provided email address, checks for existing
    subscriptions, and creates a new subscription if valid. Sends
    a confirmation email upon successful subscription.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Redirects back to the referring page.
    """
    if request.method == "POST":
        email = request.POST.get('email')

        # Validate email format
        validator = EmailValidator()
        try:
            validator(email)
        except ValidationError:
            messages.error(
                request, "Invalid email address. Please enter a valid email."
            )
            return redirect(request.META.get('HTTP_REFERER', '/'))

        # Check if the email already exists
        if NewsletterSubscription.objects.filter(email=email).exists():
            messages.error(
                request, "You have already subscribed to our newsletter!"
            )
        else:
            try:
                # Create the subscription
                NewsletterSubscription.objects.create(email=email)

                # Send confirmation email
                send_newsletter_confirmation_email(email)

                messages.success(
                    request, "Thank you for subscribing to our newsletter!"
                )
            except Exception as e:
                # Handle unexpected errors during email sending
                messages.error(request, f"An error occurred: {str(e)}")

    # Redirect back to the referring page
    return redirect(request.META.get('HTTP_REFERER', '/'))
