# Use the official Python image from the Docker Hub
FROM --platform=linux/x86-64 python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . /app/

# Expose the port the app runs on
EXPOSE 8100

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8100"]