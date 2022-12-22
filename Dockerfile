FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY requirments.txt .
RUN pip install -r requirments.txt
COPY . .
CMD python manage.py runserver 0.0.0.0:80
