from rest_framework.views import APIView
import stripe
from amirbin import settings
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect
from users.models import User

products = {'Premium': 'price_1JDCyVB9cEHLnTYOxmajeYKc', 'Unlimited': 'price_1JDD1JB9cEHLnTYOn9k5yFz1'}

class StripeKeyView(APIView):
    def get(seld, request):
        return Response({'stripe_key': settings.STRIPE_PUBLISHABLE_KEY}, status=status.HTTP_200_OK)

class CheckoutSessionCreationView(APIView):
    def post(self, request, product_name):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        price_id = products[product_name]
        
        try:
            checkout_session = stripe.checkout.Session.create(
                client_reference_id= # request.user.id if request.user.is_authenticated else None,
                success_url= settings.FRONTEND_URL + 'notes/1/',
                cancel_url= settings.FRONTEND_URL + 'notes/2/',
                payment_method_types=['card'],
                mode='subscription',
                line_items=[
                    {
                        'price': price_id,
                        'quantity': 1,
                    }
                ]
            )
            return Response({'sessionId': checkout_session['id']}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)