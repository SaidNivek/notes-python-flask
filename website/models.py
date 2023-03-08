# import . will import from the current package, which is the website folder, from init.py
from . import db
# Custom class that we can inherit from flask_login that will give our user some specific things for our flask login
from flask_login import UserMixin

# To define a db object, we create the class in the singular and inherit from db.model (db we imported above)
# For this model, we are also inheriting from UserMixin
class User(db.model, UserMixin):
    # In here, we define all of the columns that we want to store in the db
    # AKA a schema in other programming languages
    # id is the primary key for this database table
    id = db.Column(db.Integer, primary_key=True)
    # When you define a string, yo ualso need to define a max length for that string
    # unique=True means that no user can have the same email as a nother user
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))