FROM python:3.8.6
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY dev-requirements.txt /code/
RUN pip install -r dev-requirements.txt
COPY . /code/
RUN python manage.py migrate
