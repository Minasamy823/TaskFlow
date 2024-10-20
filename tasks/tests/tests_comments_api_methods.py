import pytest
from rest_framework.reverse import reverse
from tasks.models import Task, Comment


@pytest.mark.django_db
class TestTaskViews:

    def test_create_comment(self, api, task: Task):
        response = api.post(
            reverse('task-comments-post', args=(task.pk,)),
            {
                "content": "Test comment",
                "task_id": task.pk
            },
            expected_status_code=201
        )
        assert response['content'] == "Test comment"

    def test_list_comments(self, api, task: Task, comment: Comment):
        response = api.get(
            reverse('task-comments-list', args=(task.pk,)),
            expected_status_code=200
        )
        assert len(response) == 1
