from app import db

class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    burritos = db.relationship('Burrito', secondary='burrito_orders', primaryjoin='Order.id == burrito_orders.c.order_id', secondaryjoin='Burrito.id == burrito_orders.c.burrito_id', backref='orders')
    
    def __repr__(self):
        return f"<Order: id: {self.id}>"