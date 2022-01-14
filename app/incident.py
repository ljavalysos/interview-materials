"""Defines Emergency Incident model."""

import random

from faker import Faker
import sqlalchemy
from sqlalchemy.dialects.sqlite import JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine('sqlite:///./incident.db')
Session = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base(bind=engine)

Column = sqlalchemy.Column
Integer = sqlalchemy.Integer
String = sqlalchemy.String
DateTime = sqlalchemy.DateTime


class Incident(Base):

    __tablename__ = 'incident'

    id = Column(Integer, primary_key=True)
    phone_number = Column(String(128), nullable=False)
    location = Column(JSON)
    emergency_type = Column(String(256))
    status = Column(String(256))
    created_time = Column(DateTime, default=sqlalchemy.func.now())


# Define enums
EMERGENCY_TYPES = [
    'fire',
    'burglary',
    'vehicle_crash'
]
STATUSES = [
    'awaiting_dispatch',
    'responders_dispatched',
    'on_scene'
]


def init_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


def populate_data():
    fake = Faker()
    session = Session()

    incidents = []
    for _ in range(25):
        incident = Incident(
            phone_number=fake.phone_number(),
            location={
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [
                        float(fake.longitude()),
                        float(fake.latitude())
                    ]
                }
            },
            emergency_type=random.choice(EMERGENCY_TYPES),
            status=random.choice(STATUSES)
        )
        print(incident.phone_number)
        incidents.append(incident)

    session.add_all(incidents)
    session.commit()
