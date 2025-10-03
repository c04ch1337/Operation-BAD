# Mission Control - Soldier and Battalion Management
import random
from config import INSTALLATIONS, MISSION_ACTIONS, SOLDIER_CONFIG

class Soldier:
    def __init__(self, name, rank, role, color, specialty):
        self.name = name
        self.rank = rank
        self.role = role
        self.color = color
        self.specialty = specialty
        self.x = random.randint(100, 924)
        self.y = 150
        self.status = "AWAITING ORDERS"
        self.current_mission = "WAR_ROOM"
        self.target_x = INSTALLATIONS[self.current_mission]["x"]
        self.target_y = INSTALLATIONS[self.current_mission]["y"]
        self.speed = random.uniform(
            SOLDIER_CONFIG["speed_min"], 
            SOLDIER_CONFIG["speed_max"]
        )
        self.medals = []
        
    def advance(self):
        # Move toward target installation
        if self.x < self.target_x:
            self.x += self.speed
        elif self.x > self.target_x:
            self.x -= self.speed
            
        if self.y < self.target_y:
            self.y += self.speed
        elif self.y > self.target_y:
            self.y -= self.speed
        
        # Check if reached destination
        if abs(self.x - self.target_x) < 8 and abs(self.y - self.target_y) < 8:
            self.execute_mission()
            return True  # Mission completed
        return False
    
    def execute_mission(self):
        # Update status based on current mission
        if self.current_mission in MISSION_ACTIONS:
            self.status = random.choice(MISSION_ACTIONS[self.current_mission])
        
        # Move to next mission in sequence
        missions = list(INSTALLATIONS.keys())
        current_index = missions.index(self.current_mission)
        next_index = (current_index + 1) % len(missions)
        self.current_mission = missions[next_index]
        
        # Update target coordinates
        self.target_x = INSTALLATIONS[self.current_mission]["x"]
        self.target_y = INSTALLATIONS[self.current_mission]["y"]
        
        # Add tactical dispersion
        self.x += random.randint(-30, 30)
        self.y += random.randint(-30, 30)
        
        # Chance to earn medal
        if random.random() < 0.1:  # 10% chance per mission
            self.medals.append("🏅")
            if len(self.medals) > 3:  # Limit medals display
                self.medals.pop(0)
    
    def communicate(self):
        # Military-style radio transmissions
        transmissions = [
            f"MOVING TO {self.current_mission.replace('_', ' ')}",
            "MISSION ACCOMPLISHED - READY FOR NEXT ORDERS",
            f"DEPLOYING {self.specialty.upper()} PROTOCOLS",
            "AWAITING YOUR SITUATION REPORT", 
            "ALL SYSTEMS OPERATIONAL - PROCEEDING TO NEXT PHASE",
            "REQUESTING PERMISSION TO ADVANCE",
            "TARGET ACQUIRED - EXECUTING ORDERS"
        ]
        return f"📻 {random.choice(transmissions)}"
    
    def draw(self):
        # Draw soldier as tactical unit
        screen.draw.filled_circle((self.x, self.y), 12, self.color)
        screen.draw.filled_circle((self.x, self.y), 8, "white")
        
        # Draw rank and name
        rank_abbr = self.rank.split()[0][:3] + "."
        screen.draw.text(f"{rank_abbr} {self.name}", 
                        (self.x-35, self.y+15), color='white', fontsize=14)
        screen.draw.text(self.status, (self.x-60, self.y+35), color='yellow', fontsize=12)
        
        # Draw medals if any
        medal_text = " ".join(self.medals)
        if medal_text:
            screen.draw.text(medal_text, (self.x-20, self.y-35), color='gold', fontsize=20)

class Battalion:
    def __init__(self):
        self.soldiers = self.deploy_battalion()
        
    def deploy_battalion(self):
        # Deploy initial soldier roster
        soldiers = [
            Soldier("Carter", "General", "CEO", "gold", "Strategic Command"),
            Soldier("Miller", "Colonel", "CTO", "crimson", "Technical Operations"),
            Soldier("Davis", "Captain", "Lead Developer", "blue", "Code Deployment"),
            Soldier("Rodriguez", "Sergeant", "QA Specialist", "green", "Quality Assurance"),
            Soldier("Jenkins", "Specialist", "Data Analyst", "purple", "Intelligence Gathering"),
            Soldier("Zhang", "Major", "Project Manager", "orange", "Mission Coordination")
        ]
        return soldiers
    
    def update_all(self):
        mission_completions = 0
        
        for soldier in self.soldiers:
            if soldier.advance():
                mission_completions += 1
            
            # Random communications
            if random.random() < SOLDIER_CONFIG["communication_chance"]:
                soldier.status = soldier.communicate()
            
            # Random crisis events
            if random.random() < SOLDIER_CONFIG["crisis_chance"]:
                soldier.status = "🚨 CRISIS: DEPLOYING COUNTERMEASURES"
                soldier.color = "red"
        
        return mission_completions
    
    def draw_all(self):
        for soldier in self.soldiers:
            soldier.draw()