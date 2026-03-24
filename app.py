from flask import Flask, request, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
from datetime import datetime
import os
import yaml

# Initialize Flask app
app = Flask(__name__)

# Configure SQLite database
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(BASE_DIR, "orders.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_SORT_KEYS'] = False

# Initialize extensions
db = SQLAlchemy(app)

# Load Swagger spec from YAML file
with open(os.path.join(BASE_DIR, 'swagger.yaml'), 'r') as f:
    swagger_config = yaml.safe_load(f)

# Initialize Flasgger
swagger = Swagger(app, template=swagger_config, template_file=None)

# ==================== MODEL ====================
class Order(db.Model):
    __tablename__ = 'order'
    
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'content': self.content,
            'created': self.created.isoformat() if self.created else None
        }

# ==================== ERROR HANDLERS ====================
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request'}), 400

# ==================== ROUTES ====================

@app.route('/orders', methods=['GET'])
def list_orders():
    orders = Order.query.order_by(Order.created.desc()).all()
    return jsonify({
        'count': len(orders),
        'orders': [order.to_dict() for order in orders]
    }), 200

@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    
    if not data or 'content' not in data:
        return jsonify({'error': 'Missing required field: content'}), 400
    
    content = data['content'].strip()
    
    if not content:
        return jsonify({'error': 'Content cannot be empty'}), 400
    if len(content) > 100:
        return jsonify({'error': 'Content must be 100 characters or less'}), 400
    
    new_order = Order(content=content)
    db.session.add(new_order)
    db.session.commit()
    
    return jsonify(new_order.to_dict()), 201

@app.route('/orders/<int:id>', methods=['GET'])
def get_order(id):
    order = Order.query.get(id)
    
    if not order:
        return jsonify({'error': 'Order not found'}), 404
    
    return jsonify(order.to_dict()), 200

@app.route('/orders/<int:id>', methods=['PUT'])
def update_order(id):
    order = Order.query.get(id)
    
    if not order:
        return jsonify({'error': 'Order not found'}), 404
    
    data = request.get_json()
    
    if not data or 'content' not in data:
        return jsonify({'error': 'Missing required field: content'}), 400
    
    content = data['content'].strip()
    
    if not content:
        return jsonify({'error': 'Content cannot be empty'}), 400
    if len(content) > 100:
        return jsonify({'error': 'Content must be 100 characters or less'}), 400
    
    order.content = content
    db.session.commit()
    
    return jsonify(order.to_dict()), 200

@app.route('/orders/<int:id>', methods=['DELETE'])
def delete_order(id):
    order = Order.query.get(id)
    
    if not order:
        return jsonify({'error': 'Order not found'}), 404
    
    db.session.delete(order)
    db.session.commit()
    
    return '', 204

# ==================== INITIALIZATION ====================
def init_db():
    with app.app_context():
        db.create_all()
        print("Database initialized successfully!")

# ==================== MAIN ====================
if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)