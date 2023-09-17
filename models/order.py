from app import db

class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(64))
    customer_phone_number = db.Column(db.String(64))
    customer_street_name = db.Column(db.String(64))
    burritos = db.relationship('Burrito_order', backref='order')

    def __repr__(self):
        return f"<Order: id: {self.id}, customer_name: {self.customer_name}, customer_phone_number: {self.customer_phone_number}, customer_street_name: {self.customer_street_name}>"