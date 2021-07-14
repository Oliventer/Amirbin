import pytest
from tokens.tasks import send_mail
import tokens
import requests
import environ

env = environ.Env(
    DEBUG=(bool, False)
)

pytestmark = [pytest.mark.django_db]


def test_send_mail_task(mocker):
    mocker.patch('requests.post')
    send_mail.apply(['test@test.com', 'login', 'kwazilink'])
    requests.post.assert_called_once_with(f"https://api.mailgun.net/v3/sandbox{env('MAILGUN_DOMAIN_NAME')}.mailgun.org/messages",
                                auth=("api", env('MAILGUN_API_KEY')),
                                data={"from": f"Amirbin Api <postmaster@sandbox{env('MAILGUN_DOMAIN_NAME')}.mailgun.org>",
                                      "to": f"test@test.com",
                                      "subject": f"Amirbin login",
                                      "html": f"Click on the link for login: kwazilink" })
