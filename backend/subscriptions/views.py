from rest_framework.views import APIView
from amirbin import settings
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect
from users.models import User
import stripe
from subscriptions.services.stripe_checkout import StripeCheckoutService
from rest_framework.permissions import IsAuthenticated
from subscriptions.models import StripeCustomer
from subscriptions.services.stripe_payment_handler import PaymentHandlingService

class StripeKeyView(APIView):
    def get(seld, request):
        return Response({'stripe_key': settings.STRIPE_PUBLISHABLE_KEY}, status=status.HTTP_200_OK)

class CheckoutSessionCreationView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, product_name):
        try:
            checkout_session = StripeCheckoutService(request.user.id, product_name)()
            return Response({'sessionId': checkout_session['id']}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

class StripeWebhook(APIView):
    def post(self, request):
        try:
            PaymentHandlingService(request.body, request.META['HTTP_STRIPE_SIGNATURE'])()
        except ValueError:
            return Response(status=400)
        except stripe.error.SignatureVerificationError:
            return Response(status=400)

        return Response(status=200)
