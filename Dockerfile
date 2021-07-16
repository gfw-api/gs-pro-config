FROM python:3.6-alpine
MAINTAINER info@vizzuality.com

ENV NAME proconfig
ENV USER proconfig

RUN apk update && apk upgrade && \
   apk add --no-cache --update bash git openssl-dev build-base alpine-sdk \
   libffi-dev postgresql-dev gcc python3-dev musl-dev g++

RUN addgroup $USER && adduser -s /bin/bash -D -G $USER $USER

RUN pip install --upgrade pip
RUN pip install gunicorn gevent

RUN mkdir -p /opt/$NAME

COPY tox.ini /opt/$NAME/tox.ini
COPY requirements.txt /opt/$NAME/requirements.txt
COPY requirements_dev.txt /opt/$NAME/requirements_dev.txt
RUN cd /opt/$NAME && pip install -r requirements.txt
RUN cd /opt/$NAME && pip install -r requirements_dev.txt

COPY entrypoint.sh /opt/$NAME/entrypoint.sh
COPY main.py /opt/$NAME/main.py
COPY gunicorn.py /opt/$NAME/gunicorn.py

# Copy the application folder inside the container
WORKDIR /opt/$NAME
COPY ./$NAME /opt/$NAME/$NAME
COPY ./tests /opt/$NAME/tests
RUN chown -R $USER:$USER /opt/$NAME

# Tell Docker we are going to use this ports
EXPOSE 6700
USER $USER

# Launch script
ENTRYPOINT ["./entrypoint.sh"]
