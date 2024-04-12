# Use Python 3.8 base image
FROM python:3.8

# Set working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY python.py /app/python.py

# Expose the port on which the server is running
EXPOSE 8000

# Command to run the Python script
CMD ["python", "python.py"]
