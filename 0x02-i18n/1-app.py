#!/usr/bin/env python3
"""
Basic Flask app setup for ALX backend project.
"""

from flask import Flask, render_template
from flask_babel  import Babel

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

@app.route('/')
def index():
    """Route to render the home page."""
    return render_template('1-index.html')

if __name__ == "__main__":
    app.run(debug=True)