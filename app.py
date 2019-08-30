from flask import Flask
from datetime import datetime
import re

app = Flask(__name__)

@app.route("/")
def home():
    return """
        this is some real shid
        uwu bean
    """

@app.route("/uwu")
def enter():
    return "General Kenobi (<a href='/'>til baka</a>)"

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)