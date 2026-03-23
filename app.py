from flask import Flask, redirect, request
from flask_swagger_ui import get_swaggerui_blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

class MyOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"Order {self.id}"

@app.route('/health-check')
def health_check():
    return "Everything going as planned"

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        current_order = request.form['content']
        new_order = MyOrder(content=current_order)
        try:
            db.session.add(new_order)
            db.session.commit()
            return redirect("/")
        except Exception as e:
            print(f"ERROR:{e}")
            return f"ERROR:{e}"
    else:
        orders = MyOrder.query.order_by(MyOrder,created).all()
        return "Hello, World"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)