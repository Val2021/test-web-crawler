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

# # run server
# ENTRYPOINT scrapy crawl g1  --host 0.0.0.0 --port 8000

EXPOSE 80

#CMD ["scrapy","crawl", "estate", "--host", "0.0.0.0", "--port", "8000"]
CMD [ "python3", "./go-spider.py" , "--host", "0.0.0.0", "--port", "8000"]
