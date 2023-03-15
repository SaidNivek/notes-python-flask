from flask import Flask
# We need this for the SQL database that we are going to use for this project
from flask_sqlalchemy import SQLAlchemy
# os stands for Operating System
from os import path

# Initialize a new database
# This is the object we are going to use whenever we need to use a database for a user, for notes, etc.
db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app=Flask(__name__)
    # Will encrypt/secure the cookies and session associated with the website
    app.config['SECRET_KEY'] = 'apples bananas cats dogs puppies smooches children'
    # Our SQL Lite database is stored at the location {DB_NAME}
    # This tells the app where we can find the database for this program
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # This gives the app to the database, so it knows what app is using it
    db.init_app(app)

    from .views import views
    from .auth import auth

    # We must register the imported views to their url_prefix, which will tell the website where to go when that url is hit
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # We need to make sure that we load this file runs and defines these classes before we initialize and create our database
    from .models import User, Note

    # use the app.appcontext() function to check to see if a database ealready exists
    # If it does not exist, the context will create a database
    # Flask-SQLAlchemy 3 no longer accepts an 'app' argument as a method, instead, it requires an active Flask application context
    with app.app_context():
        db.create_all()
        print('Database created!')

    return app