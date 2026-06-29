# id - integer, primary key, auto increments
# name - string
# neighbourhood - string
# latitude - decimal
# longitude - decimal
# capacity - integer
# busyness_score - integer (0-100)
# A model in SQLAlchemy looks like this pattern:
# A model is a Python class that represents a table in your database. Each attribute on the class is a column in the table.

from app import db


class Venue(db.Model):
    # Primary key — auto increments
    id = db.Column(db.Integer, primary_key=True)

    # Basic info
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200))
    neighbourhood = db.Column(db.String(100))

    # Location coordinates
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    # Venue details
    capacity = db.Column(db.Integer)
    num_screens = db.Column(db.Integer)
    opening_hours = db.Column(db.String(50))
    cover_charge = db.Column(db.Float)

    # Crowd data (live later, hardcoded for now)
    busyness_score = db.Column(db.Integer)

    def __repr__(self):
        return f'<Venue {self.name}>'
