from flask import Flask
from flask_wtf.csrf import CSRFProtect
from routes import main_bp


def create_app():
    # Create the Flask app instance
    app = Flask(__name__)

    # Load the configuration class
    app.config['SECRET_KEY'] = 'yoursupersecrettokenhere'

    # Initialize extensions
    csrf = CSRFProtect(app)

    # Register blueprints
    app.register_blueprint(main_bp)

    return app
