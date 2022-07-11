# base image
FROM python:3.8-slim

# install dependencies
RUN apt-get update && \
    apt-get -y install gcc libpq-dev python-dev git wget unzip

# set working directory
WORKDIR /usr/src/app

#COPY shared archives
RUN python -m pip install --upgrade setuptools

#add and install requirements
COPY requirements.txt /usr/src/app/requirements.txt

#COPY shared archives
RUN pip install -r requirements.txt


# add app
COPY . /usr/src/app

ENTRYPOINT python3 /usr/src/app/go-spider.py
