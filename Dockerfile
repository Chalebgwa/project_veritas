# Use the official Python image as the base image
FROM python:3.9.6

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install project dependencies in the virtual environment
RUN python3 -m venv venv
RUN /bin/bash -c "source venv/bin/activate && pip install -r requirements.txt"

# Copy your Django project into the container
COPY . /app/

# Expose the port your application will run on
EXPOSE 8000

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
