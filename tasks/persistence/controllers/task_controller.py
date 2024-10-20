from base import RequestManager
from filters_fields import TASK_FILTER_FIELDS
from tasks.persistence.repositories.task_repository import TaskRepository
from tasks.persistence.repositories.taskfile_repository import TaskFileRepository


class TaskController:
    _request_manager = RequestManager()

    @staticmethod
    def create_task(data, user):
        return TaskRepository.create_task(data, user)

    @staticmethod
    def get_task(task_id):
        return TaskRepository.get_task_by_id(task_id)

    @staticmethod
    def update_task(task, data):
        return TaskRepository.update_task(task, data)

    @staticmethod
    def delete_task(task):
        return TaskRepository.delete_task(task)

    @classmethod
    def list_tasks(cls, request):
        filters = cls._request_manager.build_filters_from_request(
            request,
            TASK_FILTER_FIELDS
        )
        return TaskRepository.list_tasks(filters)

    @staticmethod
    def attach_files(task_id: int, files: list):
        return TaskFileRepository.create_task_file(task_id, files)
