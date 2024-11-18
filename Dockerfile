FROM python:3.10.12-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/usr/backend_app/.

WORKDIR /usr/backend_app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    && pip install --upgrade pip \
    && pip install poetry

ADD pyproject.toml /usr/backend_app/

RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction --no-ansi

COPY src ./src
