FROM python:3.11.9-alpine3.20

WORKDIR /python-scripts
COPY . /python-scripts
RUN pip install -r requirements.txt
