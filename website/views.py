# Store the standard routes for our websites, where the user can navigate to
# Whenever we want to render a template, must import render_template function
from flask import Blueprint, render_template

# This file is a blueprint of our application
views=Blueprint('views', __name__)

# Whenever we go to the main page of our website (/), whatever is inside the home function will run
@views.route('/')
def home():
    return render_template('home.html')
    # To render a template, we return the render_template function and then the name of the html template