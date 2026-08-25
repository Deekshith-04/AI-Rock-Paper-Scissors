"""
=========================================
Gesture Predictor
=========================================
Loads the trained model and predicts
Rock / Paper / Scissors.
"""

import joblib
import numpy as np

from config import (
    MODEL_PATH,
    CONFIDENCE_THRESHOLD
)


class GesturePredictor:

    def __init__(self):

        self.model = joblib.load(MODEL_PATH)

    # -------------------------------------

    def predict(self, landmarks):

        if landmarks is None:
            return "Unknown", 0.0

        data = np.array(landmarks).reshape(1, -1)

        probabilities = self.model.predict_proba(data)[0]

        confidence = float(np.max(probabilities))

        prediction = self.model.predict(data)[0]

        # Reject weak predictions
        if confidence < CONFIDENCE_THRESHOLD:
            return "Unknown", confidence

        return prediction, confidence