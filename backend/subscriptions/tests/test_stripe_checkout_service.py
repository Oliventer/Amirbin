import pytest
from amirbin import settings
from subscriptions.services.stripe_checkout import StripeCheckoutService

pytestmark = [pytest.mark.django_db]


"""assert response.data['sessionId'][0:8] == 'cs_test_'
    assert len(response.data['sessionId']) == 66"""


def test_session_creation(user):
    session = StripeCheckoutService(user.id, 'Premium')()
    assert session.id[0:8] == 'cs_test_'
    assert len(session.id) == 66 
  

def test_session_do_not_creates_with_bad_product_name(user):
    with pytest.raises(KeyError):
        session = StripeCheckoutService(user.id, 'bad_name')()
    

def test_session_metadata(user):
    session = StripeCheckoutService(user.id, 'Premium')()
    assert session.metadata['subscription_name'] == "P"
      

def test_session_urls(user):
    session = StripeCheckoutService(user.id, 'Premium')()
    assert session.success_url == settings.FRONTEND_URL + 'success'
    assert session.cancel_url == settings.FRONTEND_URL + 'cancel'