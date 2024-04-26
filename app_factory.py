from flask import Flask
from routes import main_bp
from config import get_config


def create_app():
    # Create the Flask app instance
    app = Flask(__name__)

    config = get_config()

    app.config.from_mapping(config)

    # Register blueprints
    app.register_blueprint(main_bp)

    return app
