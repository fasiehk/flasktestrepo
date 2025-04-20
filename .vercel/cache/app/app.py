from app import create_app
from app.routes import shortener_bp

app = create_app()
app.register_blueprint(shortener_bp)

if __name__ == "__main__":
    app.run(debug=True)