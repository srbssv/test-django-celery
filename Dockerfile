# syntax=docker/dockerfile:1

FROM python:3.10.5-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /proj
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
