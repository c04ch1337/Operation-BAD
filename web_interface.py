# Web Interface for Operation B.A.D.
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
        self.render("templates/mission_status.html")

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    clients = set()
    battalion = Battalion()
    
    def open(self):
        self.clients.add(self)
        print("Mission Control Connected")
    
    def on_message(self, message):
        # Handle commands from web interface
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
        # Broadcast update to all connected clients
        for client in cls.clients:
            client.send_status()

def make_app():
    return tornado.web.Application([
        (r"/", MissionHandler),
        (r"/websocket", WebSocketHandler),
        (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "assets"}),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    print("🚀 Operation B.A.D. Web Interface running on http://localhost:8000")
    
    # Update battalion every second
    periodic = tornado.ioloop.PeriodicCallback(WebSocketHandler.update_battalion, 1000)
    periodic.start()
    
    tornado.ioloop.IOLoop.current().start()