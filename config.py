# Operation B.A.D. Configuration File
# Mission Parameters and Installation Layout

# Display Settings
WIDTH = 1024
HEIGHT = 768
TITLE = "Operation B.A.D. - Business Army Development"

# Military Installations (Development Phases)
INSTALLATIONS = {
    "WAR_ROOM": {
        "x": 150, 
        "y": 500, 
        "color": "darkgreen", 
        "name": "WAR ROOM\n(Strategy)"
    },
    "TRAINING_SIM": {
        "x": 350, 
        "y": 500, 
        "color": "navy", 
        "name": "TRAINING SIM\n(Development)"
    },
    "FIELD_OPS": {
        "x": 550, 
        "y": 500, 
        "color": "darkred", 
        "name": "FIELD OPS\n(Testing)"
    },
    "INTEL_CENTER": {
        "x": 750, 
        "y": 500, 
        "color": "purple", 
        "name": "INTEL CENTER\n(Analytics)"
    },
    "COMMAND_POST": {
        "x": 450, 
        "y": 300, 
        "color": "gold", 
        "name": "COMMAND POST\n(Review)"
    }
}

# Soldier Configuration
SOLDIER_CONFIG = {
    "speed_min": 0.8,
    "speed_max": 1.5,
    "communication_chance": 0.015,
    "crisis_chance": 0.005
}

# Mission Parameters
MISSION_ACTIONS = {
    "WAR_ROOM": [
        "ANALYZING BUSINESS OBJECTIVES",
        "FORMULATING STRATEGIC PLAN", 
        "COORDINATING MISSION PARAMETERS",
        "ASSESSING CLIENT REQUIREMENTS"
    ],
    "TRAINING_SIM": [
        "DEPLOYING AI SOLDIERS",
        "RUNNING SIMULATION DRILLS",
        "OPTIMIZING AGENT PERFORMANCE",
        "CALIBRATING AI MODELS"
    ],
    "FIELD_OPS": [
        "EXECUTING LIVE OPERATIONS",
        "GATHERING FIELD INTELLIGENCE", 
        "TESTING UNDER FIRE",
        "VALIDATING SOLUTIONS"
    ],
    "INTEL_CENTER": [
        "ANALYZING MISSION DATA",
        "GENERATING INTELLIGENCE REPORTS",
        "IDENTIFYING OPPORTUNITIES",
        "PROCESSING PERFORMANCE METRICS"
    ],
    "COMMAND_POST": [
        "BRIEFING COMMAND",
        "REVIEWING MISSION SUCCESS",
        "PLANNING NEXT DEPLOYMENT",
        "APPROVING STRATEGIC MOVES"
    ]
}