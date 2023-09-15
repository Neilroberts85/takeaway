from app import db

class Customer(db.Model):
    __tablename__ = "customers"
    id = db.Column(db.Integer, primarykey=True)
    name = db.Column(db.String(64))
    phone_number = db.Column(db.Integer)
    street_name = db.Column(db.String(64))

    def __repr__(self):
        return f"<Customer: id: {self.id}, name: {self.name}, phone_number: {self.phone_number}, street_name: {self.street_name}>"