from notepad.services.upload import UploadService
from notepad.services.notes_limit import NotesLimitError
import pytest
from notepad.models import Note
from mixer.backend.django import mixer
from rest_framework.test import APIClient
from freezegun import freeze_time
from notepad.tasks import cleaner

pytestmark = [pytest.mark.django_db]


@pytest.fixture
def user():
    return mixer.blend('users.User', email='oliventer@gmail.com', subscription='B')


@pytest.fixture
def api(user):
    client = APIClient()
    client.force_authenticate(user=user)
    return client

@pytest.fixture
def mock_allowed_amount(monkeypatch):
    patched = {'B': 0}
    monkeypatch.setattr('notepad.services.notes_limit.allowed_amount', patched)


def test_service_object_create_valid_instance(user):
    UploadService(user, 'Грузите апельсины бочками')()
    assert Note.objects.last().code == 'Грузите апельсины бочками'
    
def test_notes_limit_service(user, mock_allowed_amount):
    with pytest.raises(NotesLimitError):
        UploadService(user, 'test')()
         

def test_model_instance_creation(api):
    api.post('/notes/', {'code': 'NewIdea', 'delete_after_viewing': False})
    assert Note.objects.last().code == 'NewIdea'


def test_delete_after_first_view(api):
    api.post('/notes/', {'code': 'Does not matter', 'delete_after_viewing': True})
    note_id = Note.objects.last().note_id
    api.get(f'/notes/{note_id}/')
    with pytest.raises(Note.DoesNotExist):
        Note.objects.get(pk=note_id)


def test_upload_endpoint(api):
    with open('upl.txt', 'rb') as f:
        response = api.post('/notes/upload/', {'file': f})
    assert response.status_code == 201
    assert Note.objects.last().code == 'Графиня изменившимся лицом бежит пруду'


def test_update_request_does_not_work(api):
    api.post('/notes/', {'code': 'Hello', 'delete_after_viewing': False})
    api.put(f'/notes/{Note.objects.last().note_id}', {'code': 'world!', 'delete_after_viewing': False})
    assert Note.objects.last().code == 'Hello'


def test_celery_deletes_30day_instances(api):
    with freeze_time("2020-01-14"):
        api.post('/notes/', {'code': 'CeleryPower', 'delete_after_viewing': False})
    cleaner.apply()
    assert Note.objects.count() == 0
