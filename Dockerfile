FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 5000

CMD ["sh", "-c", "python db_init.py && gunicorn -w 2 -b 0.0.0.0:5000 app:app"]

