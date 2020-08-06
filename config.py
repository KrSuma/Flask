"""
config.py
"""
"""
it is in general a good practice to set configuration from environment variables,
and provide a fallback value when the env does not define the var.
"""

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # secret key for security
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # Flask-SQLAlchemy configuration
    # takes the location of the application's database from this config var
    # check_same_thread seems to solve the threading error
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db?check_same_thread=False')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Email configuration
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TSL') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['jaesun90@gmail.com']


