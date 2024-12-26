# Imports
from flask import Flask, render_template, Response
from inference_classifier import video_stream

app = Flask(__name__)

# Route to stream video
@app.route('/video_feed')
def video_feed():
    return Response(video_stream(), mimetype='multipart/x-mixed-replace; boundary=frame')   # mimetype = defining the nature of the video stream

# Routes for your website
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/learning')
def test():
    return render_template('learning.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
