FROM ubuntu:22.04
LABEL maintainer seanchang
RUN mkdir /medical
WORKDIR /medical
COPY requirements.txt requirements.txt
USER root
RUN apt-get update && apt-get install -y python3-pip
RUN pip install --upgrade pip
RUN pip install -r requirements.txt