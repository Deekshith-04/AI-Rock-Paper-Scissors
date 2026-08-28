# Testing Guide

## Overview

The AI Rock Paper Scissors project was tested to verify that the hand tracking, gesture recognition, game logic, and overall gameplay work correctly.

Testing was performed using the webcam and different Rock, Paper, and Scissors hand gestures.

## Gesture Recognition Testing

The gesture recognition system was tested using the three supported gestures:

- Rock
- Paper
- Scissors

For each gesture, the hand was placed in front of the webcam and the predicted result was checked.

The system successfully detected the hand landmarks and passed the extracted features to the trained machine learning model.

## Dataset Testing

The gesture recognition model was trained using a custom dataset containing:

- 500 Rock samples
- 500 Paper samples
- 500 Scissors samples

Total samples:

```text
1500