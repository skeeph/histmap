FROM python:3.6-slim

RUN mkdir /opt/app
RUN apt-get update && apt-get install -y build-essential \
    nginx netcat binutils libproj-dev gdal-bin
ADD requirements.txt /opt/app
COPY requirements /opt/app/requirements

RUN cd /opt/app && pip install -r requirements.txt

RUN apt-get purge -y build-essential && apt-get autoremove -y
WORKDIR /opt/app