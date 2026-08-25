# Gesture Recognition Model

## Overview

The AI Rock Paper Scissors project uses a machine learning model to recognize the player's hand gesture from hand landmark data.

The model classifies the input into one of three classes:

- Rock
- Paper
- Scissors

## Hand Landmark Features

The hand tracking system detects **21 landmarks** on a single hand.

Each landmark contains three values:

- X coordinate
- Y coordinate
- Z coordinate

Therefore, the model receives:

```text
21 landmarks × 3 coordinates = 63 features