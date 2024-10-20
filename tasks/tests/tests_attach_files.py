import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.reverse import reverse

from tasks.models import Task, TaskFile


@pytest.mark.django_db
def test_attach_files_to_task(api, task: Task):
    file = SimpleUploadedFile("testfile.txt", b"This is a test file.")

    response = api.post(
        reverse("task-attach-files", args=(task.pk,)),
        data={'files': [file]},
        format='multipart',
        expected_status_code=200
    )

    assert response['message'] == 'Files attached successfully'

    assert TaskFile.objects.filter(task=task).count() == 1


@pytest.mark.django_db
def test_attach_files_to_non_existing_task(api):
    file = SimpleUploadedFile("testfile.txt", b"This is a test file.")

    response = api.post(
        reverse("task-attach-files", args=(0000,)),
        files={'files': [file]},
        format='multipart',
        expected_status_code=404
    )
    assert response['detail'] == 'Not found.'


