from django.db import models
from cuser.models import AbstractCUser

class SubscriptionType(models.TextChoices):
    BASIC = 'B'
    PREMIUM = 'P'
    UNLIMITED = 'U'

class User(AbstractCUser):
    password = None
    subscription = models.TextField(choices=SubscriptionType.choices, default='B')
   