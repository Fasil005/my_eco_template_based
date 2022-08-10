# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

# RUN chown mysql:8 /var/run/mysqld

# RUN mkdir -p /Users/me/docker/mysql/data
# RUN chmod -R 777 /Users/me/docker/mysql/data
