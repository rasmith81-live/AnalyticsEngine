# Multi-stage Dockerfile for Multi-Microservice Pattern

FROM python:3.11-slim AS base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    gcc \
    g++ \
    libpq-dev \
    gosu \
    openssl \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip wheel && \
    pip install --no-cache-dir -r requirements.txt

# Copy entrypoint script and make it executable
COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

# Copy application code
COPY . .

# Pre-install metadata_ingestion_service dependencies including large spaCy model
# This avoids runtime installation of the ~560MB model
RUN pip install --no-cache-dir -r services/business_services/metadata_ingestion_service/requirements.txt

# Build argument for service directory
ARG SERVICE_DIR
ENV SERVICE_DIR=${SERVICE_DIR}

# Create a non-root user with home directory
RUN groupadd -r appuser && useradd -r -g appuser -m -d /home/appuser appuser
RUN chown -R appuser:appuser /app
RUN chown -R appuser:appuser /home/appuser

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

# Run the application
# Dynamic entrypoint detection:
# 1. Install service-specific requirements if present
# 2. Check for __init__.py (module pattern) vs app/ subdirectory (app pattern)
CMD ["sh", "-c", "cd ${SERVICE_DIR} && \
    if [ -f requirements.txt ]; then echo 'Installing service dependencies...'; pip install --no-cache-dir --user -r requirements.txt; fi && \
    export PATH=\"/home/appuser/.local/bin:$PATH\" && \
    if [ -f __init__.py ] && [ -f main.py ]; then \
        echo 'Starting service as Python module...'; \
        SERVICE_NAME=$(basename $(pwd)) && \
        cd /app/services/$(dirname ${SERVICE_DIR#services/}) && \
        uvicorn ${SERVICE_NAME}.main:app --host 0.0.0.0 --port 8000; \
    elif [ -d app ]; then \
        echo 'Starting service from app.main...'; \
        export PYTHONPATH=$(pwd):$PYTHONPATH && \
        uvicorn app.main:app --host 0.0.0.0 --port 8000; \
    else \
        echo 'Starting service from root main.py...'; \
        uvicorn main:app --host 0.0.0.0 --port 8000; \
    fi"]
