import pytest
from django.contrib.auth.models import User
from rest_framework.reverse import reverse

from tasks.models import Task


@pytest.mark.django_db
class TestTaskViews:

    def test_create_task(self, api, other_user: User):
        response = api.post(
            reverse('task-create'),
            {
                "title": "Test Task",
                "description": "This is a test task",
                "assigned_to_id": other_user.id
            },
            expected_status_code=201
        )
        assert response['title'] == "Test Task"

    def test_get_task(self, api, main_user: User, task: Task):
        response = api.get(reverse('task-retrieve', args=(task.pk,)), )
        assert response['title'] == task.title

    def test_list_tasks_with_filters(self, api, main_user: User, task: Task):
        response = api.get(
            f"{reverse('task-list')}?title={task.title}")

        assert len(response) == 1

    def test_update_task(self,
                         api,
                         main_user: User,
                         task: Task
                         ):
        response = api.put(
            reverse('task-update', args=(task.pk,)),
            {
                "title": "Updated Task",
                "description": "Updated task description",
                "assigned_to_id": main_user.id
            },
            expected_status_code=200
        )
        assert response['title'] == "Updated Task"
        assert response['assigned_to'] == str(main_user.id)

    def test_delete_task(self, api, main_user: User, task: Task):
        api.delete(
            reverse('task-delete', args=(task.pk,)),
            expected_status_code=204
        )

        assert not Task.objects.count()
