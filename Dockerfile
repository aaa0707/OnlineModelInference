FROM ubuntu:latest
COPY requirements.txt /usr/src/app/

RUN set -xe \
    && apt-get update \
    && apt-get install -y python3-pip

RUN pip3 install --no-cache-dir -r /usr/src/app/requirements.txt

COPY flask_app.py /usr/src/app/
ADD templates /usr/src/app/templates
ADD src /usr/src/app/src
ADD tmp /usr/src/app/tmp

WORKDIR /usr/src/app/

ENV FLASK_APP=flask_app
EXPOSE 5000

CMD ["python3", "flask_app.py"]

