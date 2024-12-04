FROM python:3.10

ENV PYTHONUNBUFFERED 1

RUN apt-get update

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .