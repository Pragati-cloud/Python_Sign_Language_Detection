# Python_Sign_Language_Detection


🤟 Sign Detection using Python, OpenCV, and scikit-learn
This project implements a real-time hand sign recognition system using a webcam feed. It leverages Mediapipe for hand landmark detection and scikit-learn (with a trained Random Forest Classifier) for gesture classification.

🔧 Tech Stack
Python

OpenCV – for video capture and display

Mediapipe – for hand landmark detection

scikit-learn – for model training and prediction

NumPy – for numerical operations

SciPy – for preprocessing or support functions

Pickle – to load the trained model

📦 Features
Detects hand landmarks in real-time from webcam input

Classifies custom hand signs (e.g., 'A', 'B', 'L')

Draws bounding boxes and labels on the detected hand

Lightweight and runs on CPU with TensorFlow Lite backend

🚀 How It Works
Capture video feed using OpenCV.

Detect hand landmarks using Mediapipe.

Extract features by normalizing landmark positions.

Predict the gesture using a pre-trained RandomForestClassifier.

Display the predicted gesture on the video frame.
