# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables to disable bytecode generation and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential

# Set working directory
WORKDIR /app

# Copy requirements and install Python packages
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port for the dashboard
EXPOSE 8050

# Default command (can be adjusted to run different services)
CMD ["python", "dashboard.py"]
