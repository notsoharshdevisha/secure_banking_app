from flask import Flask
from routes import main_bp
from config import get_config
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


def create_app():
    # Create the Flask app instance
    app = Flask(__name__)

    Limiter(
        get_remote_address,
        app=app,
        default_limits=["200 per day", "50 per hour"],
        storage_uri="memory://",
    )

    config = get_config()

    app.config.from_mapping(config)

    # Register blueprints
    app.register_blueprint(main_bp)

    return app
