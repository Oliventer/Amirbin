import pytest

pytestmark = [pytest.mark.django_db]


def test_endpoint(api):
    request = api.get('/paswordlessTokens/')
    assert request.status_code == 200
    