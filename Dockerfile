FROM fedora:26

COPY requirements.txt /root/requirements.txt
RUN dnf install python-pip
RUN pip install -r /root/requirements.txt
COPY . /dndApp
WORKDIR /dndApp
EXPOSE 5000
