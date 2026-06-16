# Use official Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first (for Docker layer caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Expose ports for FastAPI and Streamlit
EXPOSE 9999 8501

# Default command (overridden by docker-compose)
CMD ["uvicorn", "backend:app", "--host", "0.0.0.0", "--port", "9999"]