from datetime import datetime, timedelta
from notepad.models import Note
from backend.amirbin.celery import app


@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(10.0, cleaner.s(), name='cleaner')


@app.task
def cleaner():
    Note.objects.all().filter(created__range=["2020-01-01", datetime.now() - timedelta(days=30)]).delete()
