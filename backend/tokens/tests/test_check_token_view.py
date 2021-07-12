import pytest
from tokens.models import PaswordlessToken
from rest_framework.authtoken.models import Token

pytestmark = [pytest.mark.django_db]


@pytest.fixture
def token(user):
    return PaswordlessToken.objects.create(user=user)


def test_check_endpoint(api, token):
    request = api.get(f'/token/check/{token.token_id}/')
    assert request.status_code == 200
    

def test_check_view_create_drf_token(api, token):
    request = api.get(f'/token/check/{token.token_id}/')
    assert request.data['token'] == Token.objects.last().key
    

def test_check_view_marks_token_as_used(api, token):
    assert PaswordlessToken.objects.get(token_id=token.token_id) is not None
    
    request = api.get(f'/token/check/{token.token_id}/')
    
    with pytest.raises(PaswordlessToken.DoesNotExist):
        assert PaswordlessToken.objects.get(token_id=token.token_id)