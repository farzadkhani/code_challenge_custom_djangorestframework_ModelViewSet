# FROM public.ecr.aws/bitnami/python:3.8.11
FROM bitnami/python:3.8.15-debian-11-r16


ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Install system packages required by Wagtail and Django.
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    libpq-dev \
    # build-essential \
 && rm -rf /var/lib/apt/lists/*

# Requirements are installed here to ensure they will be cached.
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./start.sh /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

# COPY ./asgi_start.sh /asgi_start
# RUN sed -i 's/\r$//g' /asgi_start
# RUN chmod +x /asgi_start

# COPY ./celery_runner.sh /celery_runner
# RUN sed -i 's/\r$//g' /celery_runner
# RUN chmod +x /celery_runner

WORKDIR /app

# ENTRYPOINT ["/entrypoint.sh"]
