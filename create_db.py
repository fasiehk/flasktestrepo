from app import create_app, db

app = create_app()

with app.app_context():
    print("Database URI:", app.config['SQLALCHEMY_DATABASE_URI'])  # Debugging
    db.create_all()
    print("Database tables created. Ready to run the application.")
