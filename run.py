# You run run.py
# → it calls create_app()
# → create_app() lives in app/__init__.py
# → Flask starts, database connects, routes register
# → Server is live, waiting for requests

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
