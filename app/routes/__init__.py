from flask import Blueprint, jsonify, render_template
from app.models import Venue
from app.services.football import get_matches

# Initialize the venues blueprint
venues_bp = Blueprint('venues', __name__)


@venues_bp.route('/')
def index():
    return render_template('index.html')


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


@venues_bp.route('/api/venues/<int:id>')
def get_venue(id):
    venue = Venue.query.get(id)
    if not venue:
        return jsonify({'error': 'Venue not found'}), 404
    venue_single = {
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
    }
    return jsonify(venue_single)


@venues_bp.route('/api/matches/')
def get_match():
    match = get_matches()
    return jsonify(match)

