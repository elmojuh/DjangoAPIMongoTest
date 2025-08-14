FROM python:3.11-slim

WORKDIR /animals_api

COPY requirements.txt /animals_api/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /animals_api/

ENV PYTHONUNBUFFERED=1

EXPOSE 5000