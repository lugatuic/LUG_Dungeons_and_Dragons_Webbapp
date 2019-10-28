"""Configuration for Flask"""

import os


class Config(object):
    """Configuration for Flask"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'temp_secretKey'
