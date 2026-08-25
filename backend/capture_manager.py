"""
=========================================
Capture Manager
=========================================
Responsible for:
- Countdown
- Stable gesture capture
- Majority voting
"""

from collections import Counter
import time


class CaptureManager:

    def __init__(self):

        self.countdown = ["ROCK", "PAPER", "SCISSORS", "SHOW!"]

        self.capture_time = 1.0      # seconds after SHOW!
        self.required_frames = 20    # number of predictions to collect

    # -------------------------------------

    def get_countdown(self):

        return self.countdown

    # -------------------------------------

    def collect_predictions(self, predictor, tracker):

        predictions = []

        start = time.time()

        while True:

            frame, landmarks, status = tracker.get_frame()

            if frame is None:
                continue

            gesture, confidence = predictor.predict(landmarks)

            if gesture != "Unknown":
                predictions.append(gesture)

            if (
                time.time() - start >= self.capture_time
                or len(predictions) >= self.required_frames
            ):
                break

        if len(predictions) == 0:
            return "Unknown"

        final_prediction = Counter(predictions).most_common(1)[0][0]

        return final_prediction