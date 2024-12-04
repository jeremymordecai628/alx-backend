#!/usr/bin/env python3
"""
Flask app with user login simulation.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext as _

app = Flask(__name__)

# Mock user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

babel = Babel(app)

@babel.localeselector
def get_locale():
    """Determine the best match for supported languages, checking URL parameters first."""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

def get_user():
    """Retrieve user information based on login_as parameter."""
    user_id = request.args.get('login_as')
    if user_id and user_id.isdigit() and int(user_id) in users:
        return users[int(user_id)]
    return None

@app.before_request
def before_request():
    """Store user information in flask.g.user."""
    g.user = get_user()

@app.route('/')
def index():
    """Render the home page."""
    return render_template('5-index.html')

if __name__ == "__main__":
    app.run(debug=True)
