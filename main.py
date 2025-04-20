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

# Run the app locally or on Railway
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use PORT from environment variables
    app.run(debug=False, host="0.0.0.0", port=port)  # Bind to 0.0.0.0 for external access
