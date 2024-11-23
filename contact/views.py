from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

# Create your views here.
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            # Store the ticket ID in the session
            request.session['ticket_id'] = str(contact.ticket_id)
            return redirect('contact_success')
    else:
        form = ContactForm()

    return render(request, 'contact/contact_form.html', {'form': form})


def contact_success(request):
    # Retrieve and clear the ticket ID from the session
    ticket_id = request.session.get('ticket_id')
    if not ticket_id:
        # If there's no ticket ID in the session, redirect to the contact form
        return redirect('contact')
    
    # Clear the ticket ID from the session after retrieving it
    del request.session['ticket_id']
    
    return render(request, 'contact/contact_success.html', {'ticket_id': ticket_id})
