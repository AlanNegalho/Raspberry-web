#import keyword
import cv2
import numpy
import imutils
from flask import Flask, render_template, Response, stream_with_context, request

video = cv2.VideoCapture(0, cv2.CAP_V4L2)
video1 = cv2.VideoCapture(1, cv2.CAP_V4L2)
app = Flask('__name__')


def video_stream():
    while True:
        ret, frame = video.read()
        if not ret:
            break
        else:
            ret, buffer = cv2.imencode('.jpeg',frame)
            frame = buffer.tobytes()
            yield (b' --frame\r\n' b'Content-type: imgae/jpeg\r\n\r\n' + frame +b'\r\n')           

def webcam():
    while True:
        ret1, frame = video1.read()
        if not ret1:
            break
        else:
            ret1, buffer = cv2.imencode('.jpeg',frame)
            frame = buffer.tobytes()
            yield (b' --frame\r\n' b'Content-type: imgae/jpeg\r\n\r\n' + frame +b'\r\n')
                                

@app.route('/')
def camera():
    return render_template('camera.html')


@app.route('/video_feed')
def video_feed():
    return Response(video_stream(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_fed')
def video_fed():
   return Response(webcam(), mimetype='multipart/x-mixed-replace; boundary=frame')

app.run(host='10.8.30.140', port='5000', debug=False)