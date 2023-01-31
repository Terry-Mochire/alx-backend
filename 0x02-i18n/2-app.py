#!/usr/bin/env python3
"""
Get locale from request
Create a get_locale() function that returns the best match with our supported languages.
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """
    Configuration class for available languages
    default locale and timezone
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object('2-app.Config')

babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Get locale from request"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """Returns the template '2-index.html'"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
