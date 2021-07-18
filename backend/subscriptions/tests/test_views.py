import pytest
from amirbin import settings

pytestmark = [pytest.mark.django_db]


def test_stripe_key_endpoint(api):
    response = api.get('/subscribe/key/')
    assert response.status_code == 200
    assert response.data['stripe_key'] == settings.STRIPE_PUBLISHABLE_KEY
    
    
def test_checkout_session_endpoint(auth_api):
    response = auth_api.post('/subscribe/Premium/')
    assert response.status_code == 201
    assert response.data['sessionId']
    

def test_checkout_session_bad_product_name(auth_api):
    response = auth_api.post('/subscribe/bad_name/')
    assert response.status_code == 400
    
    
def test_checkout_session_unauthenticated(api):
     response = api.post('/subscribe/Premium/')
     assert response.status_code == 403


def test_webhook_endpoint(api):
    response = api.post('/stripe/webhook/', 
                        HTTP_STRIPE_SIGNATURE='TEST')
    assert response.status_code == 400
