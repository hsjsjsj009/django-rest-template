FROM python:alpine

ARG BUILD_ENV=staging

WORKDIR /opt/app

COPY . .

ENV APP_ENV=production

RUN apk add -u --no-cache gcc musl-dev linux-headers\
    libffi-dev postgresql-dev && \
    pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["gunicorn", "--bind", ":8000","drf_template.wsgi"]