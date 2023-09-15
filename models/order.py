from app import db

class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primarykey=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    burrito = db.relationship('Burrito', backref='order')

    def __repr__(self):
        return f"<Order: id: {self.id}>"