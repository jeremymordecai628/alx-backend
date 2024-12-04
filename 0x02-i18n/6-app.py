#!/usr/bin/env python3
"""
Flask app with user locale preference.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext as _

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
    """Determine the best match for supported languages."""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.before_request
def before_request():
    """Store user information in flask.g.user."""
    g.user = get_user()

@app.route('/')
def index():
    """Render the home page."""
    return render_template('6-index.html')

if __name__ == "__main__":
    app.run(debug=True)
