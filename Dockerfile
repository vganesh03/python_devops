# Use Python 3.9-slim as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file first to leverage Docker cache
COPY requirements.txt .

# Install the dependencies (including pytest for running tests)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Install pytest separately in case it's missing from requirements.txt
# (only if pytest is not included in your requirements.txt)
RUN pip install pytest

# Expose the port your app runs on (if applicable)
# EXPOSE 5000  # Uncomment if your app runs on a specific port, like Flask

# Set the default command to run when the container starts
CMD ["python", "app.py"]  # Replace with the correct entry point to your app
