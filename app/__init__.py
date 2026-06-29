# app/__init__.py
# Application factory — creates and configures the Flask app

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# SQLAlchemy instance lives outside create_app so models can import it
db = SQLAlchemy()


def create_app():
    # Create Flask app instance
    app = Flask(__name__)

    # Load database config (will move to .env later)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/watchparty_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Bind SQLAlchemy to this app
    db.init_app(app)

    # Register routes
    from app.routes import venues_bp
    app.register_blueprint(venues_bp)

    # Return configured app
    return app
