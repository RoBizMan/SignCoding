from django.shortcuts import render, redirect
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from .models import Contact


def send_contact_confirmation_email(contact):
    """
    Sends a confirmation email to the user after a successful contact
    form submission.

    Args:
        contact (Contact): The contact instance containing user details
                            for the email.
    """
    # Render email subject and body from templates
    subject = render_to_string(
        'emails/contact_confirmation_email_subject.txt', {'contact': contact}
    )
    body = render_to_string(
        'emails/contact_confirmation_email_body.html', {'contact': contact}
    )

    # Send email using Django's send_mail function
    send_mail(
        subject.strip(),  # Subject line
        '',               # Plain text body (optional)
        settings.DEFAULT_FROM_EMAIL,  # From email
        [contact.email],  # To email
        html_message=body  # HTML content
    )


def contact_view(request):
    """
    Handles the display and processing of the contact form.

    If the request method is POST, it processes the submitted form. If
    the form is valid, it saves the contact instance, sends a
    confirmation email, and redirects to a success page. If the request
    method is GET, it displays an empty contact form.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Renders the contact form or redirects to the
                        success page.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            # Send confirmation email
            send_contact_confirmation_email(contact)

            # Store the ticket ID in the session
            request.session['ticket_id'] = str(contact.ticket_id)

            # Display a success message
            messages.success(
                request, "Your message has been sent successfully! \
                Check your email for confirmation."
            )
            return redirect('contact_success')
    else:
        form = ContactForm()

    return render(request, 'contact/contact_form.html', {'form': form})


def contact_success(request):
    """
    Displays a success message after a successful contact form
    submission.

    This view retrieves and clears the ticket ID from the session. If
    no ticket ID exists in the session, it redirects to the contact
    form.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Renders the success page or redirects to the
                        contact form.
    """
    # Retrieve and clear the ticket ID from the session
    ticket_id = request.session.get('ticket_id')

    if not ticket_id:
        # If there's no ticket ID in the session, redirect to the contact form
        return redirect('contact')

    # Clear the ticket ID from the session after retrieving it
    del request.session['ticket_id']

    return render(
        request, 'contact/contact_success.html', {'ticket_id': ticket_id}
    )
