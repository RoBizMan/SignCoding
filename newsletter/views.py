from django.contrib import messages
from django.shortcuts import redirect
from .models import NewsletterSubscription

def subscribe_newsletter(request):
    if request.method == "POST":
        email = request.POST.get('email')
        if NewsletterSubscription.objects.filter(email=email).exists():
            messages.error(request, "You have already subscribed to our newsletter!")
        else:
            NewsletterSubscription.objects.create(email=email)
            messages.success(request, "Thank you for subscribing to our newsletter!")
    return redirect(request.META.get('HTTP_REFERER', '/'))  # Redirect back to the referring page
