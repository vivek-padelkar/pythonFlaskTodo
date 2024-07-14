from server import app, db  # Adjust 'server' to your script name

with app.app_context():
    db.create_all()
    print("Database tables created.")