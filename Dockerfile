# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENV IMMICH_API_URL=<API_URL>
ENV IMMICH_API_KEY=<API_KEY>

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]