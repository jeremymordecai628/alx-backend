#!/usr/bin/env python3
"""
Flask app setup with Babel for language localization.
"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)

class Config:
    """Configuration class for Babel settings."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

# Apply Config settings to the Flask app
app.config.from_object(Config)

# Instantiate the Babel object and link it to the app
babel = Babel(app)

@babel.localeselector
def get_locale():
    """Determine the best match for supported languages."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """Route to render the home page."""
    return render_template('2-index.html')

if __name__ == "__main__":
    app.run(debug=True)
