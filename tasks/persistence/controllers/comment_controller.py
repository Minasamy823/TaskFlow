from ..repositories.comment_repository import CommentRepository
from ...models import Comment


class CommentController:

    @staticmethod
    def create_comment(request, task_id: int) -> Comment:
        data = {
            'task_id': task_id,
            'author': request.user,
            'content': request.data['content']
        }
        return CommentRepository.create_comment(data)

    @staticmethod
    def list_comments(task):
        return CommentRepository.list_comments(task)
