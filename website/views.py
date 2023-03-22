# Store the standard routes for our websites, where the user can navigate to
# Whenever we want to render a template, must import render_template function
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
# json is built into python - needed for the delete_note definition below
import json

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

@views.route('delete-note', methods=['POST'])
def delete_note():
    # The request data is a string
    # the string is sent from the index.js, where the deleteNote function is defined
    note = json.loads(request.data)
    noteId = note['noteId']
    # Look for the note that has the Id of the note that is passed in
    note = Note.query.get(noteId)
    # If it exists, we can delete
    if note:
        # If the user who is signed in owns this note, then we will delete that note
        # Prevents other users from deleting all of the notes from everyone else's account
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()            
        # Return an empty response, since we do need to return something from these views   
        return jsonify({})