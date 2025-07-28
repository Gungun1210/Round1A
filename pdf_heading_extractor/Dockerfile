FROM --platform=linux/amd64 python:3.10-slim

WORKDIR /app

ENV DEBIAN_FRONTEND=noninteractive

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

RUN mkdir -p /app/output

CMD ["python", "extract_pdf.py"]
