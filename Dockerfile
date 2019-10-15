FROM alpine:latest

COPY requirements.txt /root/requirements.txt
RUN apk add python \
  gcc
run apk add py-pip
RUN pip install -r /root/requirements.txt
COPY . /dndApp
WORKDIR /dndApp
EXPOSE 5000
