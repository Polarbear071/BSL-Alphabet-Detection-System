# Imports
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)    # Standard definition of flask

@app.route('/')    # Stating the default route for the website
def home():    # defining the home page
    return render_template('index.html')    # Rendering the template within the page

@app.route('/test')
def test():
    return render_template('test.html')      # Rendering the template

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':    # Ensuring that the website wil run
    app.run(debug = True)    # 'debug = True' ensures that any changes are automatically changed upon save not re-run
