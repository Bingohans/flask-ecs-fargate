FROM python:3.11-slim

WORKDIR /app
COPY app.py .

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir flask gunicorn

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000", "--workers", "2"]
