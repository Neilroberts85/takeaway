from app import db
from models.burrito import Burrito

# should probably be called "order_item(s)" as this class/table represents an item on a order. 
class Burrito_order(db.Model):
    __tablename__ = "burrito_orders"
    id = db.Column(db.Integer, primary_key=True)
    burrito_id = db.Column(db.Integer, db.ForeignKey("burritos.id"))
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"))
    quantity = db.Column(db.Integer)
    
