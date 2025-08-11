FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

ENV PIP_NO_CACHE_DIR=1

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "analyze.py"]

