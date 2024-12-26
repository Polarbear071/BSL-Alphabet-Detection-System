# Imports
from flask import Flask, render_template, Response
from inference_classifier import video_stream

class PageData():
    def __init__(self, title, usage, complexity):
        self.title = title
        self.usage = usage  # The use of the page
        self.complexity = complexity    # What makes it complex

home = PageData('Home Page / Root Page', "Contains the 'Letter of the day' feature", 'JS countdown = 0, python code changes daily image')
learning = PageData('Learning Page', 'Used to learn BSL', 'AI functionality & ensuring the webcam appears on the page')
about = PageData('About Page', 'Used to answer FAQ', 'Nothing extraordinary to note')

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
        if counter == 26:
            counter = 0

if __name__ == '__main__':
    app.run(debug=True)