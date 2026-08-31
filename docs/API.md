# API Documentation

## Overview

The AI Rock Paper Scissors backend provides the core functionality required for gesture recognition and gameplay.

The backend is responsible for processing requests, managing the game, predicting gestures, and returning results to the frontend.

## Backend Components

The backend contains several modules:

- `app.py` - Application entry point
- `routes.py` - API routes
- `predictor.py` - Gesture prediction
- `hand_tracker.py` - Hand landmark detection
- `game_engine.py` - Game result calculation
- `statistics.py` - Game statistics management
- `config.py` - Application configuration

## Main API Flow

```text
Frontend Request
       ↓
Backend Route
       ↓
Gesture Processing
       ↓
Model Prediction
       ↓
Game Engine
       ↓
Result Response
       ↓
Frontend Display