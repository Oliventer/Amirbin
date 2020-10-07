from datetime import datetime, timedelta
from notepad.models import Note
from celery import shared_task


@shared_task
def cleaner():
    q = Note.objects.all().filter(created__range=["2020-01-01", datetime.now() - timedelta(days=30)]).delete()
    print('del')

