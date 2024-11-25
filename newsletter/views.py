from django.contrib import messages
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from .models import NewsletterSubscription

# Function to send the newsletter subscription confirmation email
def send_newsletter_confirmation_email(email):
    """
    Sends a confirmation email to the user after a successful newsletter subscription.
    """
    # Render email subject and body from templates
    subject = render_to_string('emails/newsletter_confirmation_email_subject.txt')
    body = render_to_string('emails/newsletter_confirmation_email_body.html', {'email': email})

    # Send email using Django's send_mail function
    send_mail(
        subject.strip(),  # Subject line
        settings.DEFAULT_FROM_EMAIL,  # From email
        [email],          # To email
        html_message=body  # HTML content
    )

# Newsletter subscription view
def subscribe_newsletter(request):
    if request.method == "POST":
        email = request.POST.get('email')
        if NewsletterSubscription.objects.filter(email=email).exists():
            messages.error(request, "You have already subscribed to our newsletter!")
        else:
            subscription = NewsletterSubscription.objects.create(email=email)
            # Send confirmation email
            send_newsletter_confirmation_email(subscription.email)
            messages.success(request, "Thank you for subscribing to our newsletter! Check your email for confirmation.")
    return redirect(request.META.get('HTTP_REFERER', '/'))  # Redirect back to the referring page
