from amirbin.celery import app
import requests
import environ

env = environ.Env(
    DEBUG=(bool, False)
)

@app.task
def send_mail(email, subject, link):
    requests.post(
        f"https://api.mailgun.net/v3/sandbox{env('MAILGUN_DOMAIN_NAME')}.mailgun.org/messages",
        auth=("api", env('MAILGUN_API_KEY')),
        data={"from": f"Amirbin Api <postmaster@sandbox{env('MAILGUN_DOMAIN_NAME')}.mailgun.org>",
              "to": f"{email}",
              "subject": f"Amirbin {subject}",
              "html": f"Click on the link for {subject}: {link}" })
              