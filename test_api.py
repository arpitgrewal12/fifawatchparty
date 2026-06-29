from app import create_app
from app.services.football import get_matches

app = create_app()

with app.app_context():
    get_matches()
