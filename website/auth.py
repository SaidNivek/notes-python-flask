# Store the standard routes for our websites, where the user can navigate to
from flask import Blueprint, render_template

# This file is a blueprint of our application, specifically for authentication
auth=Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up')
def sign_up():
    return render_template('sign_up.html')