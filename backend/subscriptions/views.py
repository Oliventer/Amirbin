from rest_framework.views import APIView
from amirbin import settings
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect
from users.models import User
from subscriptions.services.stripe_checkout import StripeCheckoutService
from rest_framework.permissions import IsAuthenticated


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