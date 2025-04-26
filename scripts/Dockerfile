FROM python:3.12-slim

WORKDIR /app

COPY gerar_logs.py .

RUN mkdir -p /var/log/pessoas

CMD ["python", "gerar_logs.py"]