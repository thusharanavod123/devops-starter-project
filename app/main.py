"""Main application entry point."""
from app import create_app
from app.utils.logger import setup_logger

# Setup logging
logger = setup_logger(__name__)

# Create Flask app
app = create_app()


if __name__ == '__main__':
    logger.info("Starting Flask application...")
    app.run(host='0.0.0.0', port=5000, debug=True)
