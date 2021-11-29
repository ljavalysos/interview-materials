"""
To run the server:

pip3 install -r requirements.txt
export FLASK_APP=server.py
export FLASK_ENV=development
flask run
"""
from flask import Flask, request, jsonify

from incident import Incident, Session, init_db, populate_data


# Create the app
app = Flask(__name__)

# Initialize db
init_db()
populate_data()
session = Session()


# Define the API endpoint
@app.route('/incidents', methods=['GET'])
def get_items():
    """Implements emergency incident data egress endpoint.

    Feel free to reference the following SQLAlchemy documentation:
    https://docs.sqlalchemy.org/en/14/orm/query.html

    And the following Flask docs:
    https://flask.palletsprojects.com/en/2.0.x/api/#flask.Request
    """
    # Fill in

    return jsonify()  # Add response as argument to jsonify()
