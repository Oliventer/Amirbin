from django.db import models
import uuid
from datetime import timedelta
from django.utils import timezone

def expire_date():
    return timezone.now() + timedelta(hours=1)
    

class PaswordlessToken(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True)
    valid_to = models.DateTimeField(default=expire_date)
    used = models.DateTimeField(null=True)
    
    def mark_as_used(self):
        self.used = timezone.now()
        self.save()
