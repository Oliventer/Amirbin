from notepad.models import Note
from users.models import User, SubscriptionType
from django.utils import timezone
from dateutil.relativedelta import relativedelta

allowed_amount = {'B': 200, 'P': 500, 'U': 1000}


class NotesLimitError(Exception):
    pass


class NotesLimitService:
    def __init__(self, request_user):
        self.request_user = request_user
        
    def __call__(self):
        notes_amount = Note.objects.all().filter(user=self.request_user, created__gt=timezone.now() - relativedelta(months=1)).count()
        allowed = allowed_amount[self.request_user.subscription]
        if notes_amount >= allowed:
            raise NotesLimitError
  