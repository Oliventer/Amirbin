from __future__ import absolute_import, unicode_literals
## Settigns for Celery

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amirbin.settings')

app = Celery('amirbin')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


"""
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
"""