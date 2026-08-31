# User Guide

## Overview

AI Rock Paper Scissors is a webcam-based game where the player uses real hand gestures to play against the computer.

The application uses hand tracking and machine learning to recognize the player's gesture.

## How to Start

1. Start the backend server.
2. Start the frontend application.
3. Open the game in your browser.
4. Allow camera access when prompted.
5. Position your hand in front of the camera.

## Supported Gestures

The game supports three hand gestures:

- Rock
- Paper
- Scissors

Make sure the gesture is clearly visible to the camera.

## Playing the Game

A typical game round works as follows:

1. Start a game round.
2. Show Rock, Paper, or Scissors to the camera.
3. Wait for the system to detect your hand.
4. The machine learning model predicts your gesture.
5. The computer selects its move.
6. The result is displayed.
7. The score is updated.

## Game Rules

The standard rules are used:

```text
Rock beats Scissors
Scissors beats Paper
Paper beats Rock