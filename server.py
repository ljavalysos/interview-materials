"""
To run the server:

pip3 install -r requirements.txt
export FLASK_APP=server.py
export FLASK_ENV=development
flask run
"""
import json

from faker import Faker
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy


# Create the app and configure database URI
app = Flask(__name__)
app.config.update({
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///',
    'SQLALCHEMY_TRACK_MODIFICATIONS': False, 
    'JSONIFY_PRETTYPRINT_REGULAR': False
})


# Define database and Item table
db = SQLAlchemy(app)


class Item(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)


# Initialize database
db.create_all()

# Populate some data
fake = Faker()
for i in range(599):
    db.session.add(
        Item(
            name=fake.unique.word()
        )
    )
db.session.commit()

# Print total count to server console
print(f'There are {Item.query.count()} items in total\n')


# Define the API endpoint
@app.route('/items', methods=['GET'])
def get_items():
    """Returns a list of 100 items, beginning with the start key.

    Feel free to reference the following SQLAlchemy documentation:
    https://docs.sqlalchemy.org/en/14/orm/query.html
    """
    start_key = request.args.get('start_key')

    # Fill in

    return jsonify()  # Add response as argument to jsonify()
