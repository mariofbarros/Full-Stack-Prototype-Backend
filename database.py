from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Initialize the SQLAlchemy instance
db = SQLAlchemy()

class Order(db.Model):
    __tablename__ = 'order'
    
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        """Convert order to dictionary for JSON serialization"""
        return {
            'id': self.id,
            'content': self.content,
            'created': self.created.isoformat() if self.created else None
        }

def init_database(app):
    # Configure the database URI
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(BASE_DIR, "orders.db")}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JSON_SORT_KEYS'] = False
    
    # Bind the database to the app
    db.init_app(app)
    
    # Create all tables
    with app.app_context():
        db.create_all()
        print("Database initialized successfully!")