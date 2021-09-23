from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
from celery.schedules import crontab

#


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_tutorial.settings')

app = Celery('celery_tutorial')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    from fib.tasks import calc_fib
    # Calls test('hello') every 10 seconds.
    # sender.add_periodic_task(10.0, test(), name='add every 10', )

    sender.add_periodic_task(10.0, calc_fib.s(), name='add every 10')

    # # Calls test('world') every 30 seconds
    # sender.add_periodic_task(30.0, test.s('world'), expires=10)

    # Executes every Monday morning at 7:30 a.m.
    # sender.add_periodic_task(
    #     crontab(hour=7, minute=30, day_of_week=1),
    #     test.s('Happy Mondays!'),
    # )


@app.task
def test():
    from fib.models import Fibonacci
    last_members = Fibonacci.objects.all().order_by('-pk')

    num_1, num_2 = last_members[0], last_members[1]
    new_num_1 = num_1.value + num_2.value
    index_1 = num_2.index + 1
    index_2 = index_1 + 1
    new_num_2 = new_num_1 + num_2.value

    Fibonacci.objects.create(index=index_1, value=new_num_1)
    Fibonacci.objects.create(index=index_2, value=new_num_2)
    print('fibL:', num_1, num_2)
    return new_num_1, new_num_2
