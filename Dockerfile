FROM python:3.11-slim

WORKDIR /app

# Copy requirements.txt
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/

CMD ["python", "-u", "src/main.py"]