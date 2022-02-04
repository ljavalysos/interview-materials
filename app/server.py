"""
To run the server:

pip3 install -r requirements.txt
export FLASK_APP=server.py
flask run

----------

Feel free to reference the following SQLAlchemy documentation:
https://docs.sqlalchemy.org/en/14/orm/query.html

And the following Flask docs:
https://flask.palletsprojects.com/en/2.0.x/api/#flask.Request
"""
from flask import Flask, request, jsonify

from incident import Incident, Session, init_db, populate_data
from schemas import IncidentSchema


# Create the app
app = Flask(__name__)

# Initialize db
init_db()
populate_data()


# Define the API endpoint
@app.route('/incidents', methods=['GET'])
def get_all_incidents():
    """Get all emergency incidents, sorted by most recently created."""
    session = Session()
    try:
        incidents = session.query(Incident)\
            .order_by(Incident.created_time.desc())\
            .all()
    finally:
        session.close()

    schema = IncidentSchema(many=True)
    return jsonify(schema.dump(incidents))
