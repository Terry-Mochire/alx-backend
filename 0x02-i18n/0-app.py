#!/usr/bin/env python3
from flask import Flask, render_template

"""
Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /: returns the template '0-index.html'
"""

app = Flask(__name__)


@app.route("/")
def index() -> str:
    """Returns the template '0-index.html'"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
