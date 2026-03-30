# Dockerfile

# Use the official Python 3.11 image from the Docker Hub.
FROM python:3.11

# Set the working directory in the container.
WORKDIR /app

# Copy requirements.txt to the working directory.
COPY requirements.txt .

# Install any dependencies specified in requirements.txt.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container.
COPY . .

# Make port 80 available to the world outside this container.
EXPOSE 80

# Define environment variable.
ENV NAME World

# Run bot.py when the container launches.
CMD ["python", "bot.py"]