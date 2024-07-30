# Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Set the working directory
WORKDIR /usr/src/app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Copy entrypoint script
COPY entrypoint.sh /usr/src/app/entrypoint.sh

# Make entrypoint script executable
RUN chmod +x /usr/src/app/entrypoint.sh


# Expose the application port
EXPOSE 8000

# Set entrypoint
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
