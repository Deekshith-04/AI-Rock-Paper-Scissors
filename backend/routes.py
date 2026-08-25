from flask import Blueprint, jsonify, request
import base64
import cv2
import numpy as np

from predictor import GesturePredictor
from hand_tracker import HandTracker
from game_runner import start_game, play_round

api = Blueprint("api", __name__)

predictor = GesturePredictor()
tracker = HandTracker()


# -------------------------
# Home
# -------------------------

@api.route("/")
def home():
    return jsonify({
        "project": "AI Rock Paper Scissors",
        "status": "Running"
    })


# -------------------------
# Statistics
# -------------------------

@api.route("/stats")
def stats():
    return jsonify({
        "matches": 0,
        "user": 0,
        "ai": 0,
        "draws": 0
    })


# -------------------------
# Start Game
# -------------------------

@api.route("/start")
def start():
    rounds = request.args.get("rounds", default=5, type=int)

    score = start_game(rounds)

    return jsonify({
        "status": "Game Started",
        "score": score
    })


# -------------------------
# Predict Gesture
# -------------------------

@api.route("/predict", methods=["POST"])
def predict():

    data = request.json

    if not data or "image" not in data:
        return jsonify({
            "gesture": "Unknown",
            "confidence": 0
        })

    try:
        image = data["image"]

        if "," in image:
            image = image.split(",", 1)[1]

        image = base64.b64decode(image)

        image = np.frombuffer(image, np.uint8)

        frame = cv2.imdecode(image, cv2.IMREAD_COLOR)

        if frame is None:
            return jsonify({
                "gesture": "Unknown",
                "confidence": 0,
                "status": "INVALID_IMAGE"
            })

        frame, landmarks, status = tracker.process(frame)

        gesture, confidence = predictor.predict(landmarks)

        return jsonify({
            "gesture": gesture,
            "confidence": round(confidence, 3),
            "status": status
        })

    except Exception as error:
        print("Prediction error:", error)

        return jsonify({
            "gesture": "Unknown",
            "confidence": 0,
            "status": "ERROR"
        }), 500


# -------------------------
# Play Round
# -------------------------

@api.route("/play")
def play():

    user_move = request.args.get("user_move")

    if not user_move:
        return jsonify({
            "error": "user_move is required"
        }), 400

    result = play_round(user_move)

    return jsonify(result)