#!/usr/bin/python3

from flask import Flask, render_template
from models import storage

app = Flask('web_flask')


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    states = storage.all('State')
    amenities = storage.all('Amenity')
    places = storage.all('Place')
    return render_template('100-hbnb.html',
                           states=states,
                           amenities=amenities,
                           places=places)


@app.teardown_appcontext
def teardown(exc):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
