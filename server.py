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
    start_key = request.args.get('start_key')

    # Fill in

    # TODO temp
    incidents = [
        {
            'phone_number': i.phone_number,
            'location': i.location,
            'emergency_type': i.emergency_type,
            'status': i.status,
            'created_time': i.created_time
        }
        for i in session.query(Incident).all()
    ]

    return jsonify(incidents)  # Add response as argument to jsonify()
