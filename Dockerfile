FROM python:3.11-slim

WORKDIR /app
COPY app.py .

RUN pip install -- pistols-no-cache-dir flask gunicorn

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000", "--workers", "2"]
