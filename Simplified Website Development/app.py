# Imports
from flask import Flask, render_template, Response
from inference_classifier import video_stream

class PageData:
    def __init__(self, title, usage, complexity):
        self.title = title
        self.usage = usage  # The use of the page
        self.complexity = complexity    # What makes it complex

app = Flask(__name__)
counter = 0
@app.route('/video_feed')
def video_feed():
    return Response(video_stream(), mimetype='multipart/x-mixed-replace; boundary=frame')   # mimetype = defining the nature of the video stream

@app.route('/')
def home():
    return render_template('index.html', counter = str(counter))

@app.route('/learning')
def test():
    return render_template('learning.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/countdown_reached', methods=['POST'])
def countdown_reached():
    global countdown_reached
    countdown_reached = True
    return "Countdown reached!"
    if countdown_reached:
        counter += 1
        countdown_reached = False

if __name__ == '__main__':
    app.run(debug=True)