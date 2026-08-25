# AI Rock Paper Scissors

## Overview

AI Rock Paper Scissors is a real-time computer vision game that allows a player to play Rock Paper Scissors against a computer using hand gestures.

Instead of using buttons or a keyboard, the system uses a camera to detect the player's hand, track hand landmarks, recognize the gesture, and determine the result of the game.

The three supported gestures are:

- Rock
- Paper
- Scissors

## How It Works

The application follows a real-time gesture recognition pipeline:

```text
Camera
   ↓
Hand Detection
   ↓
Hand Landmark Tracking
   ↓
Gesture Feature Extraction
   ↓
Machine Learning Model
   ↓
Rock / Paper / Scissors
   ↓
Game Engine
   ↓
Computer Move
   ↓
Game Result