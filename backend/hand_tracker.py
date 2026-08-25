"""
=========================================
Hand Tracker
=========================================
Detects a single hand and returns
normalized landmarks.
"""

import cv2
import mediapipe as mp

from config import (
    MAX_HANDS,
    MIN_DETECTION_CONFIDENCE,
    MIN_TRACKING_CONFIDENCE
)


class HandTracker:

    def __init__(self):

        self.mp_hands = mp.solutions.hands

        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=MAX_HANDS,
            min_detection_confidence=MIN_DETECTION_CONFIDENCE,
            min_tracking_confidence=MIN_TRACKING_CONFIDENCE
        )

        self.drawer = mp.solutions.drawing_utils

    # -------------------------------------

    def process(self, frame):

        # Keep live input consistent with the training dataset
        frame = cv2.flip(frame, 1)

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = self.hands.process(rgb)

        if not results.multi_hand_landmarks:
            return frame, None, "NO_HAND"

        if len(results.multi_hand_landmarks) > 1:
            return frame, None, "MULTIPLE_HANDS"

        hand = results.multi_hand_landmarks[0]

        self.drawer.draw_landmarks(
            frame,
            hand,
            self.mp_hands.HAND_CONNECTIONS
        )

        wrist = hand.landmark[0]

        landmarks = []

        for lm in hand.landmark:

            landmarks.extend([
                lm.x - wrist.x,
                lm.y - wrist.y,
                lm.z - wrist.z
            ])

        return frame, landmarks, "HAND_FOUND"