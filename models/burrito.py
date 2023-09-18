from app import db

class Burrito(db.Model):
    __tablename__ = "burritos"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    price = db.Column(db.Float)
    orders = db.relationship("Burrito_order", backref="burrito")
    # orders = db.relationship()
    
    def __repr__(self):
        return f"<Burrito: id: {self.id}, price: {self.price}>"
    


    





#  meat = db.Column(db.String(64))
#     beans = db.Column(db.String(64))
#     rice = db.Column(db.String(64))
#     salsa = db.Column(db.String(64))
#     avacado = db.Column(db.String(64))
#     cheese = db.Column(db.String(64))
#     sauce = db.Column(db.String(64))
#     price = db.Column(db.String(64))