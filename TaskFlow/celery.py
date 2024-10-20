import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TaskFlow.settings')
app = Celery('TaskFlow')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.timezone = 'Europe/Moscow'
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'check-task-reminders-every-day': {
        'task': 'tasks.tasks.check_task_reminders',
        'schedule': crontab(hour="0", minute="0"),  # Run every day at midnight
    },
}
