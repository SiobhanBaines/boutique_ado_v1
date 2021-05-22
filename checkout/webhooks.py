from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from checkout.webhook_handler import StripeWH_Handler

import stripe


@require_POST
@csrf_exempt
def webhook(request):
    """Listen for webhooks from Stripe"""
    # Setup
    wh_secret = settings.STRIPE_WH_SECRET
    print('wh_secret ', wh_secret)
    stripe.api_key = settings.STRIPE_SECRET_KEY
    print('stripe.api_key ', stripe.api_key)
    # Get the webhook data and verify its signature
    payload = request.body
    print('payload ', payload)
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    print('sig_header ', sig_header)
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
            )
        print('event ', event)

    except ValueError as e:
        # Invalid payload
        print('valueError')
        return HttpResponse(status=400)

    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        print('stripe.error.SignatureVerificationError')
        return HttpResponse(status=400)

    except Exception as e:
        print('Exception')
        return HttpResponse(content=e, status=400)

    print('Success')
    return HttpResponse(status=200)
