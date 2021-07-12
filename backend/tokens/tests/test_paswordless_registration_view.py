import pytest
from tokens.models import PaswordlessToken
from users.models import User

pytestmark = [pytest.mark.django_db]


@pytest.fixture(autouse=True)
def mock_send_mail(mocker):
    mocker.patch('tokens.tasks.send_mail.delay')
    
    
def test_registration_endpoint(api):
    request = api.get(f'/token/auth/testuser@gmailtest.com/')
    assert request.status_code == 201


def test_view_does_not_accept_registred_user(api, user):
    request = api.get(f'/token/auth/{user.email}/')
    assert request.status_code == 403
    assert request.data == {'Already registred'}
    
    
def test_view_create_user(api):
    request = api.get(f'/token/auth/testuser@gmailtest.com/')
    assert User.objects.get(email='testuser@gmailtest.com')
    

def test_view_create_token(api):
    request = api.get(f'/token/auth/testuser@gmailtest.com/')
    assert PaswordlessToken.objects.get(user__email='testuser@gmailtest.com')