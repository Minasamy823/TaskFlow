from tasks.models import TaskFile
from tasks.persistence.repositories.task_repository import TaskRepository


class TaskFileRepository:

    @staticmethod
    def create_task_file(task_id: int, files: list) -> None:
        task = TaskRepository.get_task_by_id(task_id)

        task.files.all().delete()

        for file in files:
            TaskFile.objects.create(
                task=task,
                file=file
            )
