FROM fedora:26
MAINTAINER: "Bennett Maciorowski"

COPY requirements.txt /root/requirements.txt
RUN pip install -r /root/requirements.txt
COPY . /dndApp
WORKDIR /dndApp
EXPOSE 5000
ENTRYPOINT ["/dndApp/dndApp.py"]
