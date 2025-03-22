# Use an official Python runtime as base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy files
COPY app/ /app/

# Install dependencies
RUN pip install -r /app/requirements.txt

# Expose port 5000
EXPOSE 5000

# Run the application
CMD ["python", "main.py"]