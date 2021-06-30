from django.db import models
import uuid
from datetime import timedelta
from django.utils import timezone

def expire_date():
    return timezone.now() + timedelta(hours=1)
    
class PaswordlessTokenManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(valid_to__gt=timezone.now(), used__isnull=True)

class PaswordlessToken(models.Model):
    objects = PaswordlessTokenManager()
    
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    token_id = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True)
    valid_to = models.DateTimeField(default=expire_date)
    used = models.DateTimeField(null=True)
    
    def mark_as_used(self):
        self.used = timezone.now()
        self.save()
        
    def genetate_url(self):
        return f"http://AbstractURL/auth/{str(self.token_id)}"
