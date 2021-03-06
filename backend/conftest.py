import pytest
from rest_framework.test import APIClient
from mixer.backend.django import mixer


@pytest.fixture
def api():
    return APIClient()

@pytest.fixture
def user():
    return mixer.blend('users.User', email='oliventer@gmail.com', subscription='B')

@pytest.fixture
def auth_api(api, user):
    api.force_authenticate(user=user)
    return api