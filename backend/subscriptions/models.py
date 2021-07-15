from django.db import models


class StripeCustomer(models.Model):
    user = models.OneToOneField(to='users.User', on_delete=models.CASCADE)
    stripeCustomerId = models.CharField(max_length=255)
    stripeSubscriptionId = models.CharField(max_length=255)
