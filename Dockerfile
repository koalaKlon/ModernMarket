FROM python:3.11.3-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /ModernMarket

COPY requirements.txt /ModernMarket/market/requirements.txt
RUN pip install -r /ModernMarket/market/requirements.txt

COPY . .