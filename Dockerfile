# Start from a lightweight Python base image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy dependency list and install them
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy all project files
COPY . .

# Run Flask server
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
