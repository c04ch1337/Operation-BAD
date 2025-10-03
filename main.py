import tornado.web
import tornado.ioloop
import os
import logging
import socket
import argparse
from typing import Optional

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MissionHandler(tornado.web.RequestHandler):
    def get(self):
        try:
            self.write('''
            <html>
            <head>
                <title>Operation B.A.D.</title>
                <style>
                    body { 
                        font-family: Arial, sans-serif; 
                        margin: 40px; 
                        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                        color: white;
                    }
                    .container {
                        max-width: 800px;
                        margin: 0 auto;
                        background: rgba(255,255,255,0.1);
                        padding: 30px;
                        border-radius: 10px;
                        backdrop-filter: blur(10px);
                    }
                    h1 { 
                        color: #fff; 
                        text-align: center;
                        margin-bottom: 30px;
                    }
                    code { 
                        background: rgba(0,0,0,0.3); 
                        padding: 10px 15px; 
                        border-radius: 5px;
                        display: block;
                        margin: 10px 0;
                        font-family: 'Courier New', monospace;
                    }
                    .status {
                        padding: 15px;
                        background: rgba(0,255,0,0.2);
                        border-radius: 5px;
                        margin: 20px 0;
                        text-align: center;
                    }
                    .port-info {
                        background: rgba(255,165,0,0.3);
                        padding: 10px;
                        border-radius: 5px;
                        margin: 15px 0;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>🚀 Operation B.A.D. - Main Application</h1>
                    <div class="status">
                        ✅ System Status: OPERATIONAL
                    </div>
                    <div class="port-info">
                        <strong>Port: 8011</strong> | Container: OPERATION-BAD
                    </div>
                    <p><strong>Military AI Agent Core System</strong></p>
                    <p>This is the main application container for Operation B.A.D. core functionality.</p>
                    <p>Available endpoints:</p>
                    <code>GET / - Main interface (this page)</code>
                    <code>GET /health - Health check</code>
                    <code>GET /status - System status</code>
                    <p>Web Interface available at: <a href="http://localhost:8012" style="color: #ffeb3b;">http://localhost:8012</a></p>
                </div>
            </body>
            </html>
            ''')
        except Exception as e:
            logger.error(f"Error in MissionHandler: {e}")
            self.write("<html><body><h1>Error serving content</h1></body></html>")

class HealthHandler(tornado.web.RequestHandler):
    def get(self):
        self.write({
            "status": "healthy", 
            "service": "operation-bad-main",
            "port": 8011,
            "container": "OPERATION-BAD"
        })

def make_app():
    return tornado.web.Application([
        (r"/", MissionHandler),
        (r"/health", HealthHandler),
        (r"/status", HealthHandler),
    ], debug=False)

def is_port_available(port: int) -> bool:
    """Check if a port is available for binding"""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind(('0.0.0.0', port))
            return True
    except socket.error:
        return False

def start_web_server(port: int = 8011, max_retries: int = 3) -> Optional[tornado.ioloop.IOLoop]:
    """
    Start the web server with retry logic for port conflicts
    """
    for attempt in range(max_retries):
        current_port = port + attempt
        try:
            if not is_port_available(current_port):
                logger.warning(f"Port {current_port} is not available, trying {current_port + 1}")
                continue
                
            app = make_app()
            app.listen(current_port)
            logger.info(f"🚀 Operation B.A.D. MAIN application started successfully on port {current_port}")
            logger.info(f"📍 Main interface: http://localhost:{current_port}")
            logger.info(f"📍 Health check: http://localhost:{current_port}/health")
            logger.info(f"📍 Container: OPERATION-BAD")
            
            return tornado.ioloop.IOLoop.current()
            
        except OSError as e:
            if "Address already in use" in str(e):
                logger.warning(f"Port {current_port} already in use, attempt {attempt + 1}/{max_retries}")
                continue
            else:
                logger.error(f"Failed to start server on port {current_port}: {e}")
                break
        except Exception as e:
            logger.error(f"Unexpected error starting server: {e}")
            break
    
    logger.error(f"Failed to start web server after {max_retries} attempts")
    return None

def main():
    """
    Main entry point for Operation B.A.D. main application
    """
    parser = argparse.ArgumentParser(description='Operation B.A.D. Main Application')
    parser.add_argument('--port', type=int, default=8011, help='Port to run the server on (default: 8011)')
    args = parser.parse_args()
    
    logger.info("Starting Operation B.A.D. Main Application...")
    logger.info(f"Configuring port: {args.port}")
    logger.info("Initializing military AI agent core system...")
    
    # Start web server
    ioloop = start_web_server(port=args.port)
    
    if ioloop:
        try:
            ioloop.start()
        except KeyboardInterrupt:
            logger.info("Received shutdown signal...")
        finally:
            ioloop.stop()
            logger.info("Operation B.A.D. main application stopped gracefully")
    else:
        logger.error("Failed to start main application. Exiting.")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())