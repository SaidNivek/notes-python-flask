# Store the standard routes for our websites, where the user can navigate to
# Whenever we want to render a template, must import render_template function
from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Note
from . import db

# This file is a blueprint of our application
views=Blueprint('views', __name__)

# Whenever we go to the main page of our website (/), whatever is inside the home function will run
@views.route('/', methods=['GET', 'POST'])
# Can only access this page if the user is logged in
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template('home.html', user=current_user)
    # To render a template, we return the render_template function and then the name of the html template