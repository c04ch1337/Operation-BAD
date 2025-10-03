# OPERATION B.A.D. - Business Army Development
# Mission: Visualize AI Agent Operations
import pgzrun
import random
from config import INSTALLATIONS, WIDTH, HEIGHT, TITLE
from missions.mission_control import Soldier, Battalion

class OperationBAD:
    def __init__(self):
        self.battalion = Battalion()
        self.mission_time = 0
        self.completed_missions = 0
        
    def update(self):
        self.mission_time += 1
        self.battalion.update_all()
        
        # Track completed mission cycles
        if self.mission_time % 300 == 0:  # Every 5 seconds approx
            self.completed_missions += 1
            
    def draw(self):
        # Draw tactical background
        screen.fill((20, 30, 60))
        
        # Draw tactical grid
        for x in range(0, WIDTH, 50):
            screen.draw.line((x, 0), (x, HEIGHT), (40, 40, 80))
        for y in range(0, HEIGHT, 50):
            screen.draw.line((0, y), (WIDTH, y), (40, 40, 80))
        
        # Draw military installations
        for name, info in INSTALLATIONS.items():
            screen.draw.filled_rect(Rect(info["x"]-60, info["y"], 120, 120), info["color"])
            lines = info["name"].split('\n')
            screen.draw.text(lines[0], (info["x"]-55, info["y"]+30), color='white', fontsize=16)
            screen.draw.text(lines[1], (info["x"]-45, info["y"]+50), color='white', fontsize=14)
        
        # Draw operation header
        screen.draw.text("OPERATION: B.A.D.", (20, 20), color='white', fontsize=36)
        screen.draw.text("BUSINESS ARMY DEVELOPMENT", (20, 60), color='yellow', fontsize=24)
        
        # Draw mission status
        screen.draw.text(f"ACTIVE PERSONNEL: {len(self.battalion.soldiers)}", 
                        (WIDTH-250, 20), color='lime', fontsize=20)
        screen.draw.text(f"MISSIONS COMPLETED: {self.completed_missions}", 
                        (WIDTH-280, 50), color='cyan', fontsize=18)
        screen.draw.text("MISSION: DEPLOY AGENTIC AI SOLUTIONS", 
                        (WIDTH-400, 80), color='white', fontsize=16)
        
        # Draw legend
        self.draw_legend()
        
        # Draw all soldiers
        self.battalion.draw_all()
    
    def draw_legend(self):
        screen.draw.text("RANK STRUCTURE:", (20, HEIGHT-150), color='white', fontsize=16)
        ranks = [
            "GENERAL - Strategic Command",
            "COLONEL - Technical Operations", 
            "MAJOR - Project Management",
            "CAPTAIN - Development",
            "SERGEANT - Quality Assurance",
            "SPECIALIST - Data Analysis"
        ]
        for i, rank in enumerate(ranks):
            screen.draw.text(rank, (40, HEIGHT-130 + i*20), color='white', fontsize=12)

# Initialize operation
operation = OperationBAD()

def update():
    operation.update()

def draw():
    operation.draw()

# Launch Operation!
pgzrun.go()