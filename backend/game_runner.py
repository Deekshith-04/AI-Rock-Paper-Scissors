"""
Game Runner

Controls the game and its rounds.
"""

from game_engine import GameEngine

engine = None


def start_game(total_rounds=5):
    global engine

    # Always create a completely new game
    engine = GameEngine(total_rounds)

    return engine.get_score()


def play_round(user_move):
    global engine

    if engine is None:
        engine = GameEngine(5)

    ai_move = engine.generate_ai_move()

    winner = engine.decide_winner(
        user_move,
        ai_move
    )

    result = {
        "user": user_move,
        "ai": ai_move,
        "winner": winner,
        "score": engine.get_score()
    }

    if not engine.is_game_over():
        engine.next_round()

    return result