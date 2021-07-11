from tokens.models import PaswordlessToken, expire_date
import pytest
from django.utils import timezone
from datetime import timedelta
from mixer.backend.django import mixer
from django.core.exceptions import ObjectDoesNotExist
from freezegun import freeze_time

pytestmark = [pytest.mark.django_db]


@pytest.fixture
def paswordless_token():
    return mixer.blend(PaswordlessToken, valid_to=timezone.now() - timedelta(hours=1))


def test_token_expire_after_hour():
    assert expire_date() <= timezone.now() + timedelta(hours=1)
    

def test_paswordless_token_manager(paswordless_token):
    with pytest.raises(ObjectDoesNotExist):
        token = PaswordlessToken.objects.get(token_id=paswordless_token.token_id)
    
        
def test_paswordless_token_generate_url(paswordless_token):
    assert paswordless_token.genetate_url() == f'http://AbstractURL/auth/{paswordless_token.token_id}'
    

@freeze_time("2020-10-20")    
def test_paswordless_token_used(paswordless_token):
    paswordless_token.mark_as_used()
    assert paswordless_token.used == timezone.now()