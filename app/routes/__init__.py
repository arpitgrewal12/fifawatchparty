from flask import Blueprint, jsonify
from app.models import Venue

# Initialize the venues blueprint
venues_bp = Blueprint('venues', __name__)


@venues_bp.route('/api/venues')
def get_venues():
    venues = Venue.query.all()
    venues_list = []
    for venue in venues:
        venues_list.append({
            'id': venue.id,
            'name': venue.name,
            'address': venue.address,
            'neighbourhood': venue.neighbourhood,
            'latitude': venue.latitude,
            'longitude': venue.longitude,
            'capacity': venue.capacity,
            'num_screens': venue.num_screens,
            'opening_hours': venue.opening_hours,
            'cover_charge': venue.cover_charge,
            'busyness_score': venue.busyness_score
        })
    return jsonify(venues_list)
