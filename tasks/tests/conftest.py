import pytest
from django.contrib.auth.models import User

from tasks.models import Task, Comment


@pytest.fixture
def task(mixer, main_user: User) -> Task:
    return mixer.blend(Task,
                       pk=1,
                       assigned_to=main_user
                       )


@pytest.fixture
def other_user(mixer) -> User:
    return mixer.blend(User,
                       pk=1
                       )


@pytest.fixture
def comment(mixer, task) -> Comment:
    return mixer.blend(Comment,
                       task=task
                       )
