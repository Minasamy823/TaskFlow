import logging

from celery import shared_task
from django.utils import timezone
from tasks.models import Task
from django.core.mail import send_mail

logger = logging.getLogger()


@shared_task
def check_task_reminders():
    now = timezone.now()
    tasks_to_remind = Task.objects.filter(reminder__lte=now, is_completed=False)

    for task in tasks_to_remind:
        try:
            send_mail(
                subject=f'Reminder: Task "{task.title}" is due soon!',
                message=f'This is a reminder for your task: {task.title}. It is due by {task.deadline}.',
                from_email='no-reply@myapp.com',
                recipient_list=[task.assigned_to.email],
            )
        except Exception as er:
            logger.error(er)
