# import . will import from the current package, which is the website folder, from init.py
from . import db
# Custom class that we can inherit from flask_login that will give our user some specific things for our flask login
from flask_login import UserMixin
# Importing func allows us to use sqlalchemy functions, which will make the database functions we specify easier to write and use, eliminating the need for us to write much-used functions ourselves
from sqlalchemy.sql import func

# To define a db object, we create the class in the singular and inherit from db.model (db we imported above)
# For this model, we are also inheriting from UserMixin
class User(db.model, UserMixin):
    # In here, we define all of the columns that we want to store in the db
    # AKA a schema in other programming languages
    # id is the primary key for this database table
    id = db.Column(db.Integer, primary_key=True)
    # When you define a string, you also need to define a max length for that string
    # unique=True means that no user can have the same email as a nother user
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10,000))
    # func.now uses sqlalchemy, where we imported it above, and automatically gives it the date/time of when the note is created, so we don't have to specify that date/time ourselves
    date = db.Column(db.DateTime(timezone=True), default=func.now())    
    # In order to use a foregin key, we do it by setting up a relationship between the two objects
    # For every note we are going to store the id of the User who created that note
    # We must pass the valid id of an exisiting user to the db.ForeignKey field
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
