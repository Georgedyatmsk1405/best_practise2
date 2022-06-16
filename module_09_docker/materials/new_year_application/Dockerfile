FROM python:3-slim-stretch


RUN mkdir /app
COPY static /app/static
COPY requirements.txt /app/
COPY app.py /app/
COPY templates /app/templates
RUN python -m pip install -r /app/requirements.txt



