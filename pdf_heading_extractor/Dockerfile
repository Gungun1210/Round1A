FROM --platform=linux/amd64 python:3.10-slim

WORKDIR /app

# Install required Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Run script on container startup
CMD ["python", "extract_pdf.py"]
