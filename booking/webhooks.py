import json
import stripe
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
from booking.models import Booking
from django.contrib import messages

stripe.api_key = settings.STRIPE_SECRET_KEY
endpoint_secret = settings.STRIPE_WH_SECRET

@csrf_exempt  # Disable CSRF protection for this view
@require_http_methods(["POST"])
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    event = None

    try:
        # Verify the webhook signature to ensure it's from Stripe
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return JsonResponse({'error': 'Invalid payload'}, status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return JsonResponse({'error': 'Invalid signature'}, status=400)

    # Handle the event based on the type
    if event['type'] == 'payment_intent.succeeded':
        handle_payment_intent_succeeded(event)
    elif event['type'] == 'payment_intent.payment_failed':
        handle_payment_intent_failed(event)
    else:
        # Other event types can be handled here
        print(f"Unhandled event type {event['type']}")

    return JsonResponse({'status': 'success'}, status=200)

def handle_payment_intent_succeeded(event):
    # Retrieve the payment intent and associated metadata
    payment_intent = event['data']['object']  # Contains a stripe.PaymentIntent
    stripe_pid = payment_intent['id']
    user_username = payment_intent['metadata']['user']
    tutor_firstname = payment_intent['metadata']['tutor_firstname']
    tutor_lastname = payment_intent['metadata']['tutor_lastname']

    # Find the corresponding booking
    booking = get_object_or_404(Booking, stripe_pid=stripe_pid)

    # Update booking status or perform actions related to the payment
    booking.payment_status = 'paid'
    booking.save()

    messages.success(booking.user, f"Payment was successful for your session with {tutor_firstname} {tutor_lastname}.")
    print(f"Payment successful for {user_username} with tutor {tutor_firstname} {tutor_lastname}.")

def handle_payment_intent_failed(event):
    # Handle failed payments if needed (e.g., sending a failure notification to the user)
    payment_intent = event['data']['object']
    stripe_pid = payment_intent['id']
    user_username = payment_intent['metadata']['user']
    tutor_firstname = payment_intent['metadata']['tutor_firstname']
    tutor_lastname = payment_intent['metadata']['tutor_lastname']

    # Find the corresponding booking and update payment status to failed
    booking = get_object_or_404(Booking, stripe_pid=stripe_pid)
    booking.payment_status = 'failed'
    booking.save()

    messages.error(booking.user, f"Payment failed for your session with {tutor_firstname} {tutor_lastname}. Please try again.")
    print(f"Payment failed for {user_username} with tutor {tutor_firstname} {tutor_lastname}.")