import tornado.web
import tornado.ioloop

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

if __name__ == "__main__":
    app = make_app()
    app.listen(8000)  # ← Keeping your original port 8000
    print("Web server running at http://localhost:8000")
    tornado.ioloop.IOLoop.current().start()