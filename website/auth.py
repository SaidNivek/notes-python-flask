# Store the standard routes for our websites, where the user can navigate to
# Need to import request at the top of our flask app so we can use it in the HHTP requests
from flask import Blueprint, render_template, request

# This file is a blueprint of our application, specifically for authentication
auth=Blueprint('auth', __name__)

# In order for a route to be able to accept HTTP requests, we need to add them to the methods=[], passing in a string of the requests that we want that particular route to be able to handle
@auth.route('/login', methods=['GET', 'POST'])
def login():
    # If we want to get the info sent from this form, we set data = request.form
    # When accessed inside of a route, the request variable will have the data that was sent in the request from within that route
    # By using request.form, we will be able to access the info that was in the form on that route
    data=request.form
    print(data)
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    return render_template('sign_up.html')