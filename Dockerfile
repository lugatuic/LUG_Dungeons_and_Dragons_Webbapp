FROM python:3.6-alpine

COPY requirements.txt /root/requirements.txt
RUN pip3 install -r /root/requirements.txt
COPY . /dndApp
WORKDIR /dndApp
EXPOSE 5000
