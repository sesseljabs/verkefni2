from flask import Flask
from datetime import datetime
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
        <h1>Heimasíða</h1>
        <p><a href="/sida2">Síða 2</a> ~ <a href="/sida3">Síða 3</a></p>
        <h2>CAT IS GOD</h2>

        <img src="http://loremflickr.com/600/400" />
    """

@app.route("/sida2")
def sida2():
    return """
        <h1>Síða 2</h1>
        <p><a href="/">Heimasíða</a> ~ <a href="/sida3">Síða 3</a></p>
        <h2>SURRENDER TO THE CAT</h2>

        <img src="http://loremflickr.com/600/400" />
    """

@app.route("/sida3")
def sida3():
    return """
        <h1>Síða 3</h1>
        <p><a href="/">Heimasíða</a> ~ <a href="/sida2">Síða 2</a></p>
        <h2>JOIN THE CAT CULT AT <a href="http://heavensgate.com/">cult of the cat</a></h2>

        <img src="http://loremflickr.com/600/400" />
    """

if __name__ == "__main__":
    # app.run(debug=True, use_reloader=True)
    app.run()