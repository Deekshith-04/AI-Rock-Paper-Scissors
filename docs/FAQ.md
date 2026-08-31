# Frequently Asked Questions

## What is AI Rock Paper Scissors?

AI Rock Paper Scissors is a webcam-based game that uses hand tracking and machine learning to recognize Rock, Paper, and Scissors gestures.

## How does the game recognize my hand gesture?

The application uses MediaPipe to detect hand landmarks from the webcam feed.

These landmarks are converted into numerical features and passed to the trained machine learning model, which predicts the gesture.

## Which gestures are supported?

The game supports:

- Rock
- Paper
- Scissors

## Do I need a webcam?

Yes. A webcam is required because the application uses the camera to detect hand gestures.

## Why is my gesture not detected?

Possible reasons include:

- Poor lighting
- Hand not fully visible
- Hand too far from the camera
- Fast hand movement
- Incorrect gesture position

Try placing your hand clearly in front of the camera with good lighting.

## Why is the prediction incorrect sometimes?

Machine learning predictions depend on the quality of the input.

Incorrect predictions can happen when:

- The gesture is unclear
- The hand position is unusual
- Lighting is poor
- The camera image is blurry

## How can I improve prediction accuracy?

You can improve recognition by:

- Using good lighting
- Keeping the hand clearly visible
- Making clear gestures
- Keeping the camera stable

Future improvements could include collecting more training data and retraining the model.

## What technologies are used?

The project uses:

- Python
- FastAPI
- Next.js
- MediaPipe
- Machine Learning
- GitHub

## Where is the trained model stored?

The trained gesture classification model is stored in:

```text
models/gesture_model_v3.pkl