# Website is a Python package because of the __init__.py folder that we added to it
from website import create_app

app = create_app()

# Make sure there is no space between the == or it won't work
if __name__=='__main__':
    # debug = True means that the web server will update and run changes when changes are made
    # Turn this off when it's in production
    app.run(debug = True)