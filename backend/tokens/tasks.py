from amirbin.celery import app
import requests

@app.task
def send_mail(email, subject, link):
    requests.post(
        "https://api.mailgun.net/v3/sandbox43bcf9e58ce14bc49aa68b4668eb232a.mailgun.org/messages",
        auth=("api", "4b86a8ea86619e05ffeaf11a77c0bf71-1f1bd6a9-e10f5225"),
        data={"from": "Amirbin Api <postmaster@sandbox43bcf9e58ce14bc49aa68b4668eb232a.mailgun.org>",
              "to": f"{email}",
              "subject": f"Amirbin {subject}",
              "html": f"Click on the link for {subject}: {link}" })
              