from flask import Flask

def create_app():
    app = Flask(__name__)
    # Will encrypt/secure the cookies and session associated with the website
    app.config['SECRET_KEY'] = 'apples bananas cats dogs puppies smooches children'

    return app