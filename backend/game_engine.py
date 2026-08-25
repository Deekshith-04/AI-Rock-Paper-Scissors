"""
Game Engine

Handles:
- AI Move
- Winner Logic
- Score
- Rounds
"""

import secrets
from config import GESTURES


class GameEngine:

    def __init__(self, total_rounds):
        self.total_rounds = total_rounds
        self.current_round = 1

        self.user_score = 0
        self.ai_score = 0
        self.draws = 0

    # -------------------------------------

    def generate_ai_move(self):
        return secrets.choice(GESTURES)

    # -------------------------------------

    def decide_winner(self, user_move, ai_move):

        # Normalize inputs
        user_move = user_move.strip().capitalize()
        ai_move = ai_move.strip().capitalize()

        if user_move == ai_move:
            self.draws += 1
            return "Draw"

        if (
            (user_move == "Rock" and ai_move == "Scissors")
            or (user_move == "Paper" and ai_move == "Rock")
            or (user_move == "Scissors" and ai_move == "Paper")
        ):
            self.user_score += 1
            return "User"

        self.ai_score += 1
        return "AI"

    # -------------------------------------

    def next_round(self):
        self.current_round += 1

    # -------------------------------------

    def is_game_over(self):
        return self.current_round > self.total_rounds

    # -------------------------------------

    def get_score(self):
        return {
            "user": self.user_score,
            "ai": self.ai_score,
            "draws": self.draws,
            "round": self.current_round,
            "total_rounds": self.total_rounds,
        }