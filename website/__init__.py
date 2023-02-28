from flask import Flask

def create_app():
    app = Flask(__name__)
    # Will encrypt/secure the cookies and session associated with the website
    app.config['SECRET_KEY'] = 'apples bananas cats dogs puppies smooches children'

    from .views import views
    from .auth import auth

    # We must register the imported views to their url_prefix, which will tell the website where to go when that url is hit
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app