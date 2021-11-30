# Solutions

## Server

```python
def get_items():
    """Implements emergency incident data egress endpoint.

    Feel free to reference the following SQLAlchemy documentation:
    https://docs.sqlalchemy.org/en/14/orm/query.html

    And the following Flask docs:
    https://flask.palletsprojects.com/en/2.0.x/api/#flask.Request
    """
    # Fill in

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
```
