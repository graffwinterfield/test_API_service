import os

# SQLALCHEMY_DATABASE_URI = 'sqlite:///info.db'
SQLALCHEMY_DATABASE_URI = 'postgresql://myuser:mypassword@localhost/mydatabase'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = os.urandom(20)
BABEL_DEFAULT_LOCALE = 'ru'
