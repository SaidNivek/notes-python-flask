# Store the standard routes for our websites, where the user can navigate to
from flask import Blueprint

# This file is a blueprint of our application, specifically for authentication
auth = Blueprint('auth', __name__)