"""
=========================================
Project Configuration
=========================================
Central configuration for the entire
AI Rock Paper Scissors project.
"""

# ----------------------------------------
# Camera Settings
# ----------------------------------------

CAMERA_ID = 0

# ----------------------------------------
# MediaPipe Settings
# ----------------------------------------

MAX_HANDS = 1

MIN_DETECTION_CONFIDENCE = 0.7

MIN_TRACKING_CONFIDENCE = 0.7

# ----------------------------------------
# AI Model
# ----------------------------------------

MODEL_PATH = "models/gesture_model_v3.pkl"
CONFIDENCE_THRESHOLD = 0.50

ROCK = "Rock"
PAPER = "Paper"
SCISSORS = "Scissors"

GESTURES = [
    ROCK,
    PAPER,
    SCISSORS
]

# ----------------------------------------
# Countdown
# ----------------------------------------

COUNTDOWN_WORDS = [
    "ROCK",
    "PAPER",
    "SCISSORS",
    "SHOW!"
]

COUNTDOWN_DELAY = 0.6

# ----------------------------------------
# Default Game Settings
# ----------------------------------------

DEFAULT_ROUNDS = 5

# ----------------------------------------
# Statistics File
# ----------------------------------------

STATS_PATH = "data/stats.json"