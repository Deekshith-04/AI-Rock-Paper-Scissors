# System Architecture

## Overview

AI Rock Paper Scissors is a real-time computer vision game that combines a Next.js frontend, Python backend, MediaPipe hand tracking, and a machine learning gesture classifier.

The system detects the player's hand through the camera, converts the detected hand into numerical landmark features, predicts the gesture, and sends the result to the game engine.

## Architecture

```text
                    ┌─────────────────────┐
                    │      User           │
                    │  Camera / Browser   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Next.js Frontend  │
                    │   Game Interface    │
                    └──────────┬──────────┘
                               │
                         HTTP / API
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Python Backend    │
                    │      FastAPI        │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
       ┌────────────┐   ┌────────────┐   ┌────────────┐
       │   Hand     │   │ Predictor  │   │ Game       │
       │  Tracker   │   │            │   │ Engine     │
       └─────┬──────┘   └─────┬──────┘   └─────┬──────┘
             │                │                │
             ▼                ▼                ▼
       MediaPipe        ML Model         Game Result
       Landmarks        Prediction       & Score