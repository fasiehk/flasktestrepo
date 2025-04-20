import os
from dotenv import load_dotenv
from app import create_app
from app.routes import shortener_bp

# Load environment variables from .env in local development
load_dotenv()

app = create_app()  # Use the refactored create_app function

# Register the blueprint within the app context
with app.app_context():
    app.register_blueprint(shortener_bp)

# Run the app locally
if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)  # Explicitly set host and port