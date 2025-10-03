import os
import zipfile

def create_operation_bad_with_docker():
    # Define the file structure and content (including all previous files)
    files_content = {
        # ... (include ALL previous files from earlier script) ...
        
        # Add new Docker files
        'Dockerfile': '''# Operation B.A.D. - Business Army Development
# Dockerized Military AI Agent Visualization

FROM python:3.9-slim

# Set mission parameters
WORKDIR /mission
ENV PYTHONUNBUFFERED=1
ENV DISPLAY=:0

# Install system dependencies for pygame
RUN apt-get update && apt-get install -y \\
    libsdl2-dev \\
    libsdl2-image-dev \\
    libsdl2-mixer-dev \\
    libsdl2-ttf-dev \\
    libportmidi-dev \\
    libswscale-dev \\
    libavformat-dev \\
    libavcodec-dev \\
    libfreetype6-dev \\
    python3-dev \\
    git \\
    && rm -rf /var/lib/apt/lists/*

# Copy mission files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for potential web interface
EXPOSE 8000

# Launch operation
CMD ["python", "main.py"]
''',

        'docker-compose.yml': '''version: '3.8'

services:
  operation-bad:
    build: .
    container_name: operation-bad
    environment:
      - DISPLAY=:0
    volumes:
      - /tmp/.X11-unix:/tmp/.X11-unix:rw
      - ./mission_logs:/mission/logs
    network_mode: host
    stdin_open: true
    tty: true
    restart: unless-stopped

  # Alternative web version (if we add web interface)
  operation-bad-web:
    build: .
    container_name: operation-bad-web
    ports:
      - "8000:8000"
    command: ["python", "web_interface.py"]
    restart: unless-stopped
''',

        '.dockerignore': '''__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
pip-log.txt
pip-delete-this-directory.txt
.tox
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.log
.git
.mypy_cache
.pytest_cache
.history
.DS_Store
*.db
*.sqlite3
assets/sounds/*.mp3
assets/sounds/*.wav
mission_logs/
''',

        'web_interface.py': '''# Web Interface for Operation B.A.D.
# For Docker deployment without GUI
import tornado.websocket
import tornado.web
import tornado.ioloop
import json
import asyncio
from missions.mission_control import Battalion
import time

class MissionHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('''
        <html>
        <head>
            <title>Operation B.A.D.</title>
                <style>
                    body { font-family: Arial, sans-serif; margin: 40px; }
                    h1 {color: #333; }
                    code { background: #f4f4f4; padding: 2px 6px; }
                </style>
            </head>
        <body>
            <h1>Operation B.A.D. - Web Interface</h1>
            <p>Military AI Agent Visualization</p>
            <p>Run with GUI: <code>python main.py</code></p>
        </body>
        </html>
        ''')

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    clients = set()
    battalion = Battalion()
    
    def open(self):
        self.clients.add(self)
        print("Mission Control Connected")
    
    def on_message(self, message):
        data = json.loads(message)
        if data.get('command') == 'get_status':
            self.send_status()
    
    def on_close(self):
        self.clients.remove(self)
        print("Mission Control Disconnected")
    
    def send_status(self):
        status = {
            'soldiers': [],
            'mission_time': int(time.time()),
            'completed_missions': len([s for s in self.battalion.soldiers if s.medals])
        }
        
        for soldier in self.battalion.soldiers:
            status['soldiers'].append({
                'name': soldier.name,
                'rank': soldier.rank,
                'status': soldier.status,
                'current_mission': soldier.current_mission,
                'medals': soldier.medals,
                'x': soldier.x,
                'y': soldier.y
            })
        
        self.write_message(json.dumps(status))
    
    @classmethod
    def update_battalion(cls):
        cls.battalion.update_all()
        for client in cls.clients:
            client.send_status()

def make_app():
    return tornado.web.Application([
        (r"/", MissionHandler),
        (r"/websocket", WebSocketHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    print("🚀 Operation B.A.D. Web Interface running on http://localhost:8000")
    
    periodic = tornado.ioloop.PeriodicCallback(WebSocketHandler.update_battalion, 1000)
    periodic.start()
    
    tornado.ioloop.IOLoop.current().start()
''',

        'run_docker.sh': '''#!/bin/bash
# Operation B.A.D. Docker Deployment Script

echo "🚀 Deploying Operation B.A.D. with Docker..."

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

# Build the Docker image
echo "📦 Building Docker image..."
docker build -t operation-bad .

# Run with GUI (requires X11)
if [ "$1" == "gui" ]; then
    echo "🎮 Starting with GUI interface..."
    xhost +local:docker
    docker-compose up operation-bad
elif [ "$1" == "web" ]; then
    echo "🌐 Starting web interface on port 8000..."
    docker-compose up operation-bad-web
else
    echo "Usage: ./run_docker.sh [gui|web]"
    echo "  gui - Run with graphical interface (requires X11)"
    echo "  web - Run with web interface on port 8000"
fi
''',

        'deploy.sh': '''#!/bin/bash
# Production Deployment Script for Operation B.A.D.

echo "🎯 Production Deployment: Operation B.A.D."

# Build optimized image
docker build -t operation-bad:latest .

# Deploy with docker-compose
docker-compose -f docker-compose.prod.yml up -d

echo "✅ Deployment complete!"
echo "🌐 Web Interface: http://localhost:8000"
echo "📊 Logs: docker-compose logs -f"
''',

        'docker-compose.prod.yml': '''version: '3.8'

services:
  operation-bad:
    image: operation-bad:latest
    container_name: operation-bad-prod
    ports:
      - "8000:8000"
    command: ["python", "web_interface.py"]
    restart: always
    environment:
      - PYTHONUNBUFFERED=1
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
'''
    }

    # Create directories and files
    base_dir = 'operation_bad_docker'
    
    print("🚀 Deploying Operation B.A.D. with Docker Support...")
    
    for file_path, content in files_content.items():
        full_path = os.path.join(base_dir, file_path)
        
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        
        # Write file content
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        # Make shell scripts executable
        if file_path.endswith('.sh'):
            os.chmod(full_path, 0o755)
            
        print(f"✅ Created: {full_path}")

    # Create zip file
    zip_filename = 'operation_bad_docker.zip'
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(base_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, base_dir)
                zipf.write(file_path, arcname)
    
    print(f"🎉 Operation B.A.D. with Docker successfully deployed!")
    print(f"📦 Zip file created: {zip_filename}")
    print(f"📁 Project folder: {base_dir}")
    print("\n🎯 Deployment Options:")
    print("   1. GUI Version:   ./run_docker.sh gui")
    print("   2. Web Version:   ./run_docker.sh web")
    print("   3. Production:    ./deploy.sh")
    print("\n⚡ DOCKER DEPLOYMENT READY!")

if __name__ == "__main__":
    create_operation_bad_with_docker()