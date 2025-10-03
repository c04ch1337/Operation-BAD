import tornado.web
import tornado.ioloop
import logging
import argparse

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class WebInterfaceHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('''
        <html>
        <head>
            <title>Operation B.A.D. - Web Interface</title>
            <style>
                body { 
                    font-family: Arial, sans-serif; 
                    margin: 40px; 
                    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
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
                .port-info {
                    background: rgba(255,105,180,0.3);
                    padding: 10px;
                    border-radius: 5px;
                    margin: 15px 0;
                }
                a {
                    color: #ffeb3b;
                    text-decoration: none;
                }
                a:hover {
                    text-decoration: underline;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🌐 Operation B.A.D. - Web Interface</h1>
                <div class="port-info">
                    <strong>Port: 8012</strong> | Container: OPERATION-BAD-WEB
                </div>
                <p><strong>Advanced Visualization & Monitoring Dashboard</strong></p>
                <p>This is the web interface container for Operation B.A.D. visualization and monitoring.</p>
                <p>Connected Services:</p>
                <ul>
                    <li>Main Application: <a href="http://localhost:8011">http://localhost:8011</a></li>
                    <li>Web Interface: <a href="http://localhost:8012">http://localhost:8012</a> (this page)</li>
                    <li>Frontend: <a href="http://localhost:18080">http://localhost:18080</a></li>
                    <li>Backend: <a href="http://localhost:8501">http://localhost:8501</a></li>
                </ul>
            </div>
        </body>
        </html>
        ''')

def make_app():
    return tornado.web.Application([
        (r"/", WebInterfaceHandler),
    ])

def main():
    parser = argparse.ArgumentParser(description='Operation B.A.D. Web Interface')
    parser.add_argument('--port', type=int, default=8012, help='Port to run the server on (default: 8012)')
    args = parser.parse_args()
    
    app = make_app()
    app.listen(args.port)
    
    logger.info(f"🌐 Operation B.A.D. Web Interface started on port {args.port}")
    logger.info(f"📍 Access at: http://localhost:{args.port}")
    logger.info(f"📍 Container: OPERATION-BAD-WEB")
    
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()