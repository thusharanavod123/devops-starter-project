"""Application configuration."""
import os
from datetime import timedelta


class Config:
    """Base configuration class."""
    
    # Flask settings
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    DEBUG = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    
    # Redis settings
    REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
    REDIS_PORT = int(os.environ.get('REDIS_PORT', 6379))
    REDIS_DB = int(os.environ.get('REDIS_DB', 0))
    
    # Cache settings
    CACHE_TTL = int(os.environ.get('CACHE_TTL', 300))  # 5 minutes default
    
    # Application settings
    APP_NAME = 'DevOps Showcase'
    APP_VERSION = '1.0.0'
    
    # Logging
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')


class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    LOG_LEVEL = 'DEBUG'


class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    LOG_LEVEL = 'INFO'


class TestConfig(Config):
    """Testing configuration."""
    TESTING = True
    REDIS_DB = 1  # Use different DB for tests
