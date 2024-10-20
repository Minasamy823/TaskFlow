import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from mixer.backend.django import mixer as _mixer

from api_client import DRFClient


@pytest.fixture
def mixer():
    return _mixer


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def main_user(mixer) -> User:
    user: User = mixer.blend(User,
                             username='username',
                             email='email@gmail.com',
                             is_active=True
                             )
    user.set_password("password")
    user.save()
    return user


@pytest.fixture
def api(main_user):
    _api = DRFClient()
    _api.force_authenticate(main_user)
    return _api
