from app import db

class Customer(db.Model):
    __tablename__ = "customers"
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(64))
    customer_phone_number = db.Column(db.String(64))
    customer_street_name = db.Column(db.String(64))
    orders = db.relationship('Order', backref='customer')

    def __repr__(self):
        return f"<Customer: id: {self.id}, customer_name: {self.customer_name}, customer_phone_number: {self.customer_phone_number}, customer_street_name: {self.customer_street_name}>"