import pytest
from tokens.models import PaswordlessToken
from users.models import User

pytestmark = [pytest.mark.django_db]


@pytest.fixture(autouse=True)
def mock_send_mail(mocker):
    mocker.patch('tokens.tasks.send_mail.delay')
        

def test_view_does_not_accept_unregistred_user(api):
    request = api.get('/token/login/randommail@gmail.com/')
    assert request.status_code == 404
    
    
def test_login_endpoint(api, user):
    request = api.get(f'/token/login/{user.email}/')
    assert request.status_code == 200


def test_login_view_create_token(api, user):
    request = api.get(f'/token/login/{user.email}/')
    assert PaswordlessToken.objects.get(user=user)
 