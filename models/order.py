from app import db

class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    burrito_orders = db.relationship('Burrito_order', backref="order")
    
    def __repr__(self):
        return f"<Order: id: {self.id}>"