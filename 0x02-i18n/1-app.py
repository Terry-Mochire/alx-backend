#!/usr/bin/env python3
"""
Basic Babel setup
hen instantiate the Babel object in your app.
Store it in a module-level variable named babel.
"""

from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """
    Configuration class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)


@app.route('/')
def index() -> str:
    """Returns the template '1-index.html'"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)