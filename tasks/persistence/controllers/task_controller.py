from typing import List
from django.contrib.auth.models import User
from base import RequestManager
from filters_fields import TASK_FILTER_FIELDS
from tasks.models import Task
from tasks.persistence.repositories.task_repository import TaskRepository
from tasks.persistence.repositories.taskfile_repository import TaskFileRepository


class TaskController:
    _request_manager = RequestManager()

    @staticmethod
    def create_task(data: dict, user: User) -> Task:
        return TaskRepository.create_task(data, user)

    @staticmethod
    def get_task(task_id: int) -> Task:
        return TaskRepository.get_task_by_id(task_id)

    @staticmethod
    def update_task(task: Task, data: dict) -> Task:
        return TaskRepository.update_task(task, data)

    @staticmethod
    def delete_task(task: Task) -> None:
        return TaskRepository.delete_task(task)

    @classmethod
    def list_tasks(cls, request) -> List[Task]:
        filters = cls._request_manager.build_filters_from_request(
            request,
            TASK_FILTER_FIELDS
        )
        return TaskRepository.list_tasks(filters)

    @staticmethod
    def attach_files(task_id: int, files: list) -> None:
        return TaskFileRepository.create_task_file(task_id, files)
