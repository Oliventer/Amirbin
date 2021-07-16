import stripe
from amirbin import settings
from subscriptions.models import StripeCustomer
from users.models import User


class PaymentHandlingService:
    def __init__(self, payload, sig_header):
        self.payload = payload
        self.sig_header = sig_header
    
    def __call__(self):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe_endpoint = settings.STRIPE_ENDPOINT
        
        event = stripe.Webhook.construct_event(
            self.payload, self.sig_header, stripe_endpoint
        )

        if event['type'] == 'checkout.session.completed':
            session = event['data']['object']
            
            user_email = session['customer_details'].get('email')
            subscription_type = session['metadata'].get('subscription_name')
            
            stripe_customer_id = session.get('customer')
            stripe_subscription_id = session.get('subscription')
            
            user = self.set_user_subscription(user_email, subscription_type)
            self.handle_customer_data(user, stripe_customer_id, stripe_subscription_id)
    
    def set_user_subscription(self, email, subscription_type):
        user = User.objects.get(email=email)
        user.subscription = subscription_type
        user.save()
        return user
        
    def handle_customer_data(self, user, stripe_customer_id, stripe_subscription_id):
        customer = StripeCustomer.objects.get(user=user)
        
        if customer is not None:
            customer.stripeCustomerId = stripe_customer_id
            customer.stripeSubscriptionI = stripe_subscription_id
            customer.save()
            return
            
        StripeCustomer.objects.create(
            user=user,
            stripeCustomerId=stripe_customer_id,
            stripeSubscriptionId=stripe_subscription_id,
        )
