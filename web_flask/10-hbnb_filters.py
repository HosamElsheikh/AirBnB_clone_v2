#!/usr/bin/python3
""" starts a Flask web application """
from models import *
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/hbnb_filters", strict_slashes=False)
def cities_by_states():
    """ display a HTML page with the states listed in alphabetical order """
    states = storage.all('State').values()
    amenities = storage.all('Amenity').values()
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
