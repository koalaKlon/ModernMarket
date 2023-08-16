FROM python:3.11.3-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /market

COPY requirements.txt /market/
RUN pip install -r requirements.txt

COPY . /market/
