# Use Playwright's official Python image
FROM mcr.microsoft.com/playwright/python:v1.41.0-focal

# Set working directory inside the container
WORKDIR /app

# Upgrade Python and pip
RUN apt-get update && apt-get install -y python3 python3-pip
RUN python3 -m pip install --upgrade pip setuptools wheel

# Copy requirements.txt before installing dependencies
COPY requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the rest of the application files
COPY . /app

# Install Playwright browsers
RUN playwright install --with-deps

# Set entry point for running tests
ENTRYPOINT ["pytest", "--browser", "chromium", "--html=playwright-report/report.html", "--self-contained-html"]
