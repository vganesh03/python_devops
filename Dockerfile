# Use a base image with Python installed
FROM python:3.9-slim

# Set the working directory inside the container to /app
WORKDIR /app

# Set PYTHONPATH so Python can locate the 'app' module
ENV PYTHONPATH="/app:${PYTHONPATH}"

# Copy the project files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install pytest for testing
RUN pip install pytest

# Expose port (if needed, but not required for testing)
#EXPOSE 5000

# Default command to run when the container starts (optional)
CMD ["python", "app/main.py"]
