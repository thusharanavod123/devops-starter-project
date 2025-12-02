"""Flask application initialization."""
from flask import Flask
from app.config import Config


def create_app(config_class=Config):
    """Create and configure the Flask application.
    
    Args:
        config_class: Configuration class to use
        
    Returns:
        Flask application instance
    """
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Register blueprints
    from app.routes import api, health
    app.register_blueprint(health.bp)
    app.register_blueprint(api.bp)
    
    return app
