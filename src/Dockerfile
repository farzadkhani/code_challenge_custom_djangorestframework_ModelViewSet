# FROM public.ecr.aws/bitnami/python:3.8.11
FROM bitnami/python:3.8.15-debian-11-r16


ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Install system packages required by Wagtail and Django.
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    libpq-dev \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY ./start.sh /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

WORKDIR /app
# Create a volume for static files
# VOLUME /static
