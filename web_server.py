import tornado.web
import tornado.ioloop
import os
import docker
from docker.errors import DockerException

class MissionHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('''
        <html>
        <head><title>Operation B.A.D.</title></head>
        <body>
            <h1>Operation B.A.D. - Web Interface</h1>
            <p>Military AI Agent Visualization</p>
            <p>Run with GUI: <code>python main.py</code></p>
        </body>
        </html>
        ''')

def make_app():
    return tornado.web.Application([
        (r"/", MissionHandler),
    ])

def create_operation_bad_with_docker():
    try:
        client = docker.from_env()
        print("Docker client initialized successfully")
    except DockerException as e:
        print(f"Failed to connect to Docker daemon")
        print(f"Error: {e}")
        return False
    
    try:
        dockerfile_dir = os.path.dirname(os.path.abspath(__file__))
        print(f"Building Docker image from: {dockerfile_dir}")
        
        image, build_logs = client.images.build(
            path=dockerfile_dir,
            tag="operation-bad:latest",
            rm=True
        )
        
        for chunk in build_logs:
            if 'stream' in chunk:
                print(chunk['stream'].strip())
        
        print("Docker image built successfully")
        
    except DockerException as e:
        print(f"Docker build failed")
        print(f"Error: {e}")
        return False
    
    try:
        container = client.containers.run(
            "operation-bad:latest",
            ports={'8000/tcp': 8000},
            detach=True,
            name="operation-bad-container"
        )
        
        print("Container started successfully")
        print(f"Container ID: {container.id}")
        print("Web interface available at: http://localhost:8000")
        return True
        
    except DockerException as e:
        print(f"Container startup failed")
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    print("Web server running at http://localhost:8000")
    tornado.ioloop.IOLoop.current().start()