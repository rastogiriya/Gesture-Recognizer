# Gesture Recognizer

Gesture Recognizer is a sophisticated system designed to interpret and understand human gestures, facilitating natural and intuitive communication between humans and machines. This technology enables more immersive and interactive experiences, and it also serves as a tool for Sign Language Detection, particularly American Sign Language (ASL).

## Overview

The project utilizes advanced techniques in computer vision, leveraging the MediaPipe library for hand detection. MediaPipe allows for the accurate identification of hand landmarks in pixel format, providing additional functionalities such as finger tracking and hand bounding box information.

## Data Collection

A diverse dataset was meticulously gathered, encompassing a wide range of static hand gestures and ASL symbols. Each class consists of 300 sample images, ensuring variations in hand orientations to enhance the robustness of the system.

## Training

The collected data was utilized to train the model using Google Teachable Machine. The dataset was organized into 11 different classes representing various gestures and ASL symbols. TensorFlow and Keras were employed to create and train the model, ensuring optimal accuracy and performance.

## Usage

To utilize Gesture Recognizer, simply run the Django server to access the web interface. Execute the testing file to initiate real-time recognition of predefined hand gestures for which data has been collected. Additionally, users have the flexibility to collect sample images for their desired gestures, retrain the model, and integrate the updated model into the project for real-time classification.

## Dependencies

- Python
- TensorFlow
- Keras
- MediaPipe
- Django

## How to Run

1. Install the necessary dependencies.
2. Run the Django server to launch the web interface.
3. Execute the testing file for real-time gesture recognition.
