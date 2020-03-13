import os

APP_NAME = os.environ['APP_NAME']
SECRET_KEY = os.environ['SECRET_KEY']
DB_HOST = os.environ['DB_HOST']
DB_HOST = os.environ['DB_HOST']
FLASK_DEBUG = os.environ['FLASK_DEBUG']
DB_USERNAME = os.environ['DB_USERNAME']
DB_PASSWORD = os.environ['DB_PASSWORD']
DB_DATABASE = os.environ['DB_DATABASE']
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:3306/{DB_DATABASE}"