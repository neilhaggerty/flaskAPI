FROM python:3.8-alpine

WORKDIR /code
RUN pip install pipenv
ENV FLASK_APP=server.py
ADD . .
RUN pip install -r requirements.txt
CMD flask run --host=0.0.0.0
