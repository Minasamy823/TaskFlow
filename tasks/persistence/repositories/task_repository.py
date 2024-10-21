from typing import List

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from tasks.models import Task


class TaskRepository:

    @staticmethod
    def create_task(data: dict, user: User) -> Task:
        task = Task.objects.create(**data, created_by=user)
        return task

    @staticmethod
    def get_task_by_id(task_id: int) -> Task:
        return get_object_or_404(Task, id=task_id)

    @staticmethod
    def update_task(task: Task, data: dict) -> Task:
        for key, value in data.items():
            setattr(task, key, value)
        task.save()
        return task

    @staticmethod
    def delete_task(task: Task) -> None:
        task.delete()

    @staticmethod
    def list_tasks(filters: dict) -> List[Task]:
        return Task.objects.filter(**filters)
