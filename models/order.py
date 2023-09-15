from app import db

class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    burritos = db.relationship('Burrito_order', backref='order')

    def __repr__(self):
        return f"<Order: id: {self.id}>"