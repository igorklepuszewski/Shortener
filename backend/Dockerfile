FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE shortener.settings.production

WORKDIR /backend

RUN pip install pipenv
COPY . /backend/
RUN pipenv install --system --dev
