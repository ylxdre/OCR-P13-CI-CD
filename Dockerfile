FROM python:3.11-slim

RUN apt update && apt install -y nginx

RUN pip install poetry

WORKDIR /OCLettings2

COPY pyproject.toml poetry.lock ./

COPY nginx/nginx.conf /etc/nginx/conf.d/default.conf

RUN poetry config virtualenvs.create false && \
	poetry install --no-interaction --no-ansi --no-root && \
	poetry add gunicorn

ARG DJANGO_SECRET_KEY

ENV DJANGO_SECRET_KEY=$DJANGO_SECRET_KEY

COPY . .

COPY nginx/nginx.conf /etc/nginx/conf.d/default.conf

RUN rm -rf /var/www/html* && \
	mkdir -p /run/nginx

RUN poetry run python manage.py collectstatic --noinput

EXPOSE 80

CMD service nginx start && \
	poetry run gunicorn --bind 127.0.0.1:8000 --env DJANGO_SETTINGS_MODULE=oc_lettings_site.settings oc_lettings_site.wsgi

