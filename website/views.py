# Store the standard routes for our websites, where the user can navigate to
from flask import Blueprint

# This file is a blueprint of our application
views = Blueprint('views', __name__)

# Whenever we go to the main page of our website (/), whatever is inside the home function will run
@views.route('/')
def home():
    return "<h1>Test</h1>"