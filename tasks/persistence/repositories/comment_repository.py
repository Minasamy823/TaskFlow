from tasks.models import Comment


class CommentRepository:

    @staticmethod
    def create_comment(data):
        return Comment.objects.create(**data)

    @staticmethod
    def list_comments(task):
        return task.comments.all()
