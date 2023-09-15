from app import db

class Burrito(db.Model):
    __tablename__ = "burritos"
    id = db.Column(db.Integer, primarykey=True)
    name = db.Column(db.String(64))
    price = db.Column(db.Integer)

    def __repr__(self):
        return f"<Burrito: id: {self.id}, meat: {self.meat}, beans: {self.beans}, rice: {self.rice}, salsa: {self.salsa}, avacado: {self.avacado}, cheese: {self.cheese}, sauce: {self.sauce}, price: {self.price}>"

    





#  meat = db.Column(db.String(64))
#     beans = db.Column(db.String(64))
#     rice = db.Column(db.String(64))
#     salsa = db.Column(db.String(64))
#     avacado = db.Column(db.String(64))
#     cheese = db.Column(db.String(64))
#     sauce = db.Column(db.String(64))
#     price = db.Column(db.String(64))