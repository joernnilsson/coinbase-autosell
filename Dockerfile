#Download base image ubuntu 16.04
FROM debian:jessie-slim

RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN pip3 install coinbase git+https://github.com/alimcmaster1/gdax-python

COPY autosell.py /autosell.py

CMD ["/usr/bin/python3", "/autosell.py"]
