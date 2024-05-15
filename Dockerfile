FROM python:3.12-slim-bookworm

EXPOSE 8000

WORKDIR /opt

RUN apt-get update && apt-get install --no-install-recommends -y \
    gcc \
    build-essential \
    git

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .