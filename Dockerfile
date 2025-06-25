FROM python:3.10-slim

# Cài đặt Tesseract và các thư viện cần thiết
RUN apt-get update && \
    apt-get install -y tesseract-ocr libtesseract-dev libleptonica-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Cài tiếng Việt cho Tesseract
RUN apt-get update && \
    apt-get install -y tesseract-ocr-vie && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 10000

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:10000"] 