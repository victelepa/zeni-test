# config.py
"""
Configuration classes for the Flask application. Each class configures the application
for a different environment.
"""

import os

class Config:
    """
    Base configuration with settings applicable to all environments.
    """
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    DEBUG = False
    TESTING = False
    ENV = 'production'  # Default to production

class ProductionConfig(Config):
    DATABASE_URI = os.getenv('PRODUCTION_DATABASE_URI', 'product_db')

class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'
    DATABASE_URI = os.getenv('DEVELOPMENT_DATABASE_URI', 'development_db')

class TestingConfig(Config):
    TESTING = True
    ENV = 'testing'
    DATABASE_URI = os.getenv('TESTING_DATABASE_URI', 'testing_db')
