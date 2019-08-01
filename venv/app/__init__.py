from flask import Flask
from flask import render_template

app = Flask(__name__)

# the main splash screen
# accessed by going to "serverlocation"
@app.route('/')
def splash_screen():
    return render_template('home.html')