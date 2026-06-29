from app import create_app, db
from app.models import Venue

app = create_app()

with app.app_context():
    # Clear existing venues so we don't get duplicates on re-run
    Venue.query.delete()

    venue1 = Venue(
        name="The Penalty Box",
        address="1268 Granville St, Vancouver",
        neighbourhood="Granville Strip",
        latitude=49.2756,
        longitude=-123.1319,
        capacity=150,
        num_screens=4,
        opening_hours="4pm - 2am",
        cover_charge=0.0,
        busyness_score=85
    )

    venue2 = Venue(
        name="Shark Club Sports Bar",
        address="180 W Georgia St, Vancouver",
        neighbourhood="Downtown",
        latitude=49.2807,
        longitude=-123.1157,
        capacity=300,
        num_screens=6,
        opening_hours="11am - 2am",
        cover_charge=10.0,
        busyness_score=72
    )

    venue3 = Venue(
        name="Biercraft Tap & Kitchen",
        address="1191 Commercial Dr, Vancouver",
        neighbourhood="Commercial Drive",
        latitude=49.2634,
        longitude=-123.0694,
        capacity=120,
        num_screens=2,
        opening_hours="5pm - 1am",
        cover_charge=0.0,
        busyness_score=61
    )

    venue4 = Venue(
        name="The Irish Heather",
        address="210 Carrall St, Vancouver",
        neighbourhood="Gastown",
        latitude=49.2834,
        longitude=-123.1043,
        capacity=100,
        num_screens=2,
        opening_hours="5pm - 1am",
        cover_charge=0.0,
        busyness_score=45
    )

    db.session.add(venue1)
    db.session.add(venue2)
    db.session.add(venue3)
    db.session.add(venue4)
    db.session.commit()
    print("Venues seeded successfully")
