FROM python:slim-bullseye

EXPOSE 8000

COPY requirements.txt ./

RUN pip install -r requirements.txt