from .__init__ import db  # Corrected import statement

class URL(db.Model):
    __tablename__ = 'url'

    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(2048), nullable=False)
    short_url = db.Column(db.String(128), unique=True, nullable=False)
    custom_alias = db.Column(db.String(128), unique=True, nullable=True)