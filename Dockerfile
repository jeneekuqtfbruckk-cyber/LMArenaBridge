FROM python:3.12-slim

WORKDIR /app

# Install necessary system utilities
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    build-essential \
    curl \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install OS dependencies for browsers using Playwright's helper
RUN playwright install-deps

# Create non-root user for Hugging Face Spaces (UID 1000)
RUN useradd -m -u 1000 user

# Copy the rest of the application code, assigning ownership to 'user'
COPY --chown=user:user . .

# Ensure startup script is executable
RUN chmod +x startup.sh

# Switch to the non-root user
USER user
ENV HOME=/home/user
ENV PATH="/home/user/.local/bin:${PATH}"

# Pre-fetch Camoufox browser binaries to avoid downloading on every container start
RUN python3 -m camoufox fetch

# Command to run on container start
CMD ["./startup.sh"]
