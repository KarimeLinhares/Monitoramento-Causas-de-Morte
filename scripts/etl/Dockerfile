FROM python:3.12-slim

WORKDIR /app

COPY etl.py .

RUN mkdir -p /var/log/pessoas

CMD ["python", "etl.py"]