FROM python:2.7

MAINTAINER Mush Mo <mush@pandorica.io>

RUN mkdir /monitor
RUN mkdir /etc/endpoints
WORKDIR /monitor

ADD requirements.txt /monitor/requirements.txt
RUN pip install -r requirements.txt

ADD entrypoint /monitor/entrypoint
ADD monitor.py /monitor/monitor.py

ENTRYPOINT ["/monitor/entrypoint"]
