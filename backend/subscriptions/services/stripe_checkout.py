from amirbin import settings
import stripe
from users.models import User

products = {'Premium': 'price_1JDCyVB9cEHLnTYOxmajeYKc', 'Unlimited': 'price_1JDD1JB9cEHLnTYOn9k5yFz1'}


class StripeCheckoutService:
    def __init__(self, user_id, product_name):
        self.user_id = user_id
        self.product_name = product_name
        
    def __call__(self):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        price_id = products[self.product_name]
        
        session = checkout_session = stripe.checkout.Session.create(
                client_reference_id = self.user_id, 
                success_url = settings.FRONTEND_URL + 'success',
                cancel_url = settings.FRONTEND_URL + 'cancel',
                payment_method_types =['card'],
                metadata = {'subscription_name': self.product_name[0]},
                mode ='subscription',
                line_items = [
                    {
                        'price': price_id,
                        'quantity': 1,
                    }
                ]
            )
        return session
