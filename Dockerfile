FROM python:3.11

WORKDIR /app

RUN pip install --no-cache-dir django gunicorn psycopg2-binary python-decouple faker

COPY . /app/

EXPOSE 8000

CMD ["python", "myclean/manage.py", "runserver", "0.0.0.0:8000"]