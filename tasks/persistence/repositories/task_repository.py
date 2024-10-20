from django.shortcuts import get_object_or_404
from tasks.models import Task


class TaskRepository:

    @staticmethod
    def create_task(data, user):
        task = Task.objects.create(**data, created_by=user)
        return task

    @staticmethod
    def get_task_by_id(task_id):
        return get_object_or_404(Task, id=task_id)

    @staticmethod
    def update_task(task, data):
        for key, value in data.items():
            setattr(task, key, value)
        task.save()
        return task

    @staticmethod
    def delete_task(task):
        task.delete()

    @staticmethod
    def list_tasks(filters: dict):
        return Task.objects.filter(**filters)
