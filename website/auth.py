# Store the standard routes for our websites, where the user can navigate to
# Need to import request at the top of our flask app so we can use it in the HHTP requests
#  flash is needed in order to use flask to flash messages to the screen
from flask import Blueprint, render_template, request, flash

# This file is a blueprint of our application, specifically for authentication
auth=Blueprint('auth', __name__)

# In order for a route to be able to accept HTTP requests, we need to add them to the methods=[], passing in a string of the requests that we want that particular route to be able to handle
@auth.route('/login', methods=['GET', 'POST'])
def login():
    # If we want to get the info sent from this form, we set data = request.form
    # When accessed inside of a route, the request variable will have the data that was sent in the request from within that route
    # By using request.form, we will be able to access the info that was in the form on that route
    # data=request.form
    # print(data)
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        # If the request is a POST request, we will get the following information from the form
        # Must use the request.for.get('name from form') to access the data from within that form
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 3 characters', category='error')
        elif len(firstName) < 2:
            flash('Email must be greater than 1 character', category='error')
        elif password1 != password2:
            flash('Passwords must match', category='error')
        elif len(password1) < 7 :
            flash('Password must be at least 7 characters', category='error')
        else:
            # add user to database
            flash('Account created!', category='success')

    return render_template('sign_up.html')