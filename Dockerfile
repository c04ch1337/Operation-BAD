# Operation B.A.D. - Business Army Development
# Dockerized Military AI Agent Visualization

FROM python:3.9-slim

# Set mission parameters
WORKDIR /mission
ENV PYTHONUNBUFFERED=1
ENV DISPLAY=:0

# Install system dependencies for pygame
RUN apt-get update && apt-get install -y \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libportmidi-dev \
    libswscale-dev \
    libavformat-dev \
    libavcodec-dev \
    libfreetype6-dev \
    python3-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy mission files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for potential web interface
EXPOSE 8000

# Launch operation
CMD ["python", "main.py"]