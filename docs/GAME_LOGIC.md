# Game Logic

## Overview

The AI Rock Paper Scissors game follows the standard rules of Rock Paper Scissors.

The player uses a hand gesture detected through the camera, while the computer selects its own gesture. The game engine compares both gestures and determines the result.

## Gestures

The game supports three gestures:

- Rock
- Paper
- Scissors

## Winning Rules

The rules are:

| Player | Computer | Result |
|---|---|---|
| Rock | Scissors | Player Wins |
| Paper | Rock | Player Wins |
| Scissors | Paper | Player Wins |
| Rock | Paper | Player Loses |
| Paper | Scissors | Player Loses |
| Scissors | Rock | Player Loses |
| Rock | Rock | Draw |
| Paper | Paper | Draw |
| Scissors | Scissors | Draw |

In simple terms:

```text
Rock beats Scissors
Scissors beats Paper
Paper beats Rock