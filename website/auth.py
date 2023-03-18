# Store the standard routes for our websites, where the user can navigate to
# Need to import request at the top of our flask app so we can use it in the HHTP requests
# flash is needed in order to use flask to flash messages to the screen
# redirect is to redirect the user to the home page after signing in, and url_for supports that
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
# Import the db from __init__.py to be able to use it here
from . import db
from flask_login import login_user, login_required, logout_user, current_user

# This file is a blueprint of our application, specifically for authentication
auth=Blueprint('auth', __name__)

# In order for a route to be able to accept HTTP requests, we need to add them to the methods=[], passing in a string of the requests that we want that particular route to be able to handle
@auth.route('/login', methods=['GET', 'POST'])
def login():
    # If we want to get the info sent from this form, we set data = request.form
    # When accessed inside of a route, the request variable will have the data that was sent in the request from within that route
    # By using request.form, we will be able to access the info that was in the form on that route
    # To log a user in, we have to get the data from the form 
    if request.method == 'POST':
        email=request.form.get('email')
        password=request.form.get('password')

        # the user will be set to the User from the database, getting a query, and then filtering by the email passed in, above
        # .first() will return the first result, even though there should only be one
        user = User.query.filter_by(email=email).first()
        # if there is a found user, we need to check to see if the password is equal to the hash that we have stored for that user's password
        if user:
            # Use the check_password_hash, passing in the user's password from the database AND the password from the login form
            # If the two match, then we can log the user in
            if check_password_hash(user.password, password):
                # If the passwords match, flash logged in successfully
                flash('Logged in successfully!', category='success')
                # If we find a user, pass the user into the login_user function
                # This will be stored in the flask session, set by remember=True
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect email or password. Please try again.', category='error')
        # If there is no user, let them know that there is an error
        else: 
            flash('Incorrect email or password. Please try again.', category='error')

    return render_template('login.html', user=current_user)

@auth.route('/logout')
# Cannot access this route unless the user is logged in using the @login_required decorator
@login_required
def logout():
    # Logout the user using the flask_login framework
    logout_user()
    # When a user logs out, send them back to the sign in page
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        # If the request is a POST request, we will get the following information from the form
        # Must use the request.for.get('name from form') to access the data from within that form
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 3 characters', category='error')
        elif len(first_name) < 2:
            flash('Email must be greater than 1 character', category='error')
        elif password1 != password2:
            flash('Passwords must match', category='error')
        elif len(password1) < 7 :
            flash('Password must be at least 7 characters', category='error')
        else:
            # add user to database
            # the password is being hashed for security reasons, passing in sha256, which is a hashing algorithm
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template('sign_up.html', user=current_user)