from app import db
from models.burrito import Burrito

class Burrito_order(db.Model):
    __tablename__ = "burrito_orders"
    id = db.Column(db.Integer, primary_key=True)
    burrito_id = db.Column(db.Integer, db.ForeignKey("burritos.id"))
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"))
    
  