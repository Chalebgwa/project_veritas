# Use the official Python image as the base image
FROM python:3.9.6

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy your Django project into the container
COPY veritas /app/

# Run migrations and start the server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
