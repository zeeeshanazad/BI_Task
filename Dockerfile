FROM python:3.8-slim-buster

RUN apt-get update
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .
ENTRYPOINT ["python","main.py"]