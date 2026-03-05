# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy all files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port (Render automatically sets PORT)
EXPOSE 10000

# Start command
CMD ["python", "main.py"]
