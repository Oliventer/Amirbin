from celery import Celery
from celery.schedules import crontab
from datetime import datetime, timedelta
# export DJANGO_SETTINGS_MODULE=amirbin.settings
# import django
# django.setup()
from notepad.models import Note

app = Celery('tasks', backend='redis://localhost', broker='redis://')


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(30.0, cleaner.s(), name='delete old queries')


@app.task
def cleaner():
    q = Note.objects.all().filter(created__range=["2020-01-01", datetime.now() - timedelta(days=5)]).delete()
    print('del')


@app.task
def test(arg):
    print(arg)


"""
app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'tasks.add',
        'schedule': 30.0,
        'args': (16, 16)
    },
}
app.conf.timezone = 'UTC'

"""


"""@app.task
def add(x, y):
    return x+y
"""