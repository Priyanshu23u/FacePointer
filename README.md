# Face Tracker with OpenCV and Flask

## Overview
This project uses OpenCV and Flask to track a user's face via a webcam and move the mouse cursor accordingly. The face is detected using OpenCV's pre-trained Haar Cascade classifier, and the position of the detected face is mapped to screen coordinates for controlling the mouse.

## Features
- Real-time face tracking using OpenCV
- Mouse movement controlled by face position
- Clicking functionality using face gestures
- Live video streaming via Flask web server
- Simple and lightweight implementation

## Requirements
Ensure you have the following installed before running the script:

- Python 3.x
- OpenCV
- Flask
- PyAutoGUI

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/your-repo/face-tracker.git
   cd face-tracker
   ```
2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv myenv
   source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install opencv-python flask pyautogui
   ```

## Usage
1. Run the Flask application:
   ```sh
   python app.py
   ```
2. Open a web browser and go to:
   ```
   http://127.0.0.1:5000/
   ```
3. The webcam feed will start streaming, and your mouse cursor will follow your face.
4. **Move the cursor:** Move your face left or right to control horizontal movement, and up or down for vertical movement.
5. **Click using face gestures:** If you bring your face closer to the camera, it will trigger a mouse click.
6. To stop tracking, navigate to:
   ```
   http://127.0.0.1:5000/stop_tracking
   ```

## File Structure
```
face-tracker/
│── app.py          # Main script to run the application
│── templates/
│   └── index.html  # Frontend HTML file
│── static/         # (Optional) Static assets like CSS/JS
│── README.md       # Project documentation
```

## Notes
- Ensure your webcam is working before running the script.
- The tracking accuracy depends on lighting conditions and webcam quality.
- Face gestures for clicking may need fine-tuning based on webcam sensitivity.



