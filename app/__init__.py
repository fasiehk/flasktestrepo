from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

db = SQLAlchemy()  # Initialize globally

def create_app():
    load_dotenv()  # Load environment variables

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///urls.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_secret_key')
    print("Using DB URI:", app.config['SQLALCHEMY_DATABASE_URI'])

    db.init_app(app)  # Initialize db with the app

    # Import models here to avoid circular import
    from .models import URL
    with app.app_context():
        db.create_all()  # Create database tables if they don't exist

    return app
