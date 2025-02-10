import cv2
import pyautogui
from flask import Flask, render_template, Response

app = Flask(__name__)

# Load OpenCV's pre-trained face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

class FaceTracker:
    def __init__(self):
        self.screen_width, self.screen_height = pyautogui.size()
        self.is_running = True

    def process_frame(self, frame):
        frame = cv2.flip(frame, 1)
        frame_height, frame_width, _ = frame.shape
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            center_x = x + w // 2
            center_y = y + h // 2
            cv2.circle(frame, (center_x, center_y), 5, (0, 255, 255), -1)
            
            mouse_x = self.screen_width / frame_width * center_x
            mouse_y = self.screen_height / frame_height * center_y
            pyautogui.moveTo(mouse_x, mouse_y)
        
        return frame

    def start_tracking(self):
        cap = cv2.VideoCapture(0)
        while self.is_running:
            _, frame = cap.read()
            if frame is not None:
                processed_frame = self.process_frame(frame)
                _, buffer = cv2.imencode('.jpg', processed_frame)
                frame_bytes = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
        cap.release()

    def stop_tracking(self):
        self.is_running = False

# Global face tracker
face_tracker = FaceTracker()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(face_tracker.start_tracking(), 
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/stop_tracking')
def stop_tracking():
    face_tracker.stop_tracking()
    return 'Tracking stopped'

if __name__ == '__main__':
    app.run(debug=True)
