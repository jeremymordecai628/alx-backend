#!/usr/bin/env python3
"""
Flask app with user timezone preference.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext as _
import pytz

app = Flask(__name__)

# Mock user database remains the same as in Task 5

class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

babel = Babel(app)

@babel.localeselector
def get_locale():
    locale = request.args.get('locale')
    if
