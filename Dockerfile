FROM python:3.7-alpine
RUN apk update \
  && apk add --virtual build-deps gcc python3-dev musl-dev libffi-dev \
  && apk add postgresql-dev \
  && apk add libxml2-dev libxslt-dev \
  && pip install scrapy \
  && pip install treelib

ADD . /hello_docker

WORKDIR /hello_docker

COPY . /hello_docker

CMD ["scrapy", "crawl", "hello_tree"]
