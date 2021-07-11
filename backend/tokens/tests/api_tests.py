import pytest
from tokens.models import PaswordlessToken
from rest_framework.test import APIClient
from mixer.backend.django import mixer
from rest_framework.authtoken.models import Token
from django.core.exceptions import ObjectDoesNotExist

pytestmark = [pytest.mark.django_db]


@pytest.fixture
def api(user):
    return APIClient()


@pytest.fixture
def user():
    return mixer.blend('users.User', email='oliventer@gmail.com')


@pytest.fixture
def token(user):
    return PaswordlessToken.objects.create(user=user)


def test_check_paswordless_token_endpoint(api, token):
    request = api.get(f'/token/check/{token.token_id}/')
    assert request.status_code == 200
    

def test_check_paswordless_token_view_create_drf_token(api, token):
    request = api.get(f'/token/check/{token.token_id}/')
    assert request.data['token'] == Token.objects.last().key
    

def test_check_paswordless_token_view_mark_token_as_used(api, token):
    assert PaswordlessToken.objects.get(token_id=token.token_id) is not None
    
    request = api.get(f'/token/check/{token.token_id}/')
    
    with pytest.raises(ObjectDoesNotExist):
        assert PaswordlessToken.objects.get(token_id=token.token_id)
        
    
def test_paswordless_tokens_endpoint(api):
    request = api.get('/paswordlessTokens/')
    assert request.status_code == 200
    

def test_paswordless_token_view_does_not_accept_unregistred_user(api):
    request = api.get('/token/login/randommail@gmail.com/')
    assert request.status_code == 404
    assert request.data == {'No such user registred'}
    
    
def test_paswordless_token_registration_view_does_not_accept_registred_user(api, user):
    request = api.get(f'/token/auth/{user}/')
    assert request.status_code == 406
    assert request.data == {'Already registred'}