from app import db
from models.burrito import Burrito
from models.order import Order
from models.burrito_order import Burrito_order
import click 

from flask.cli import with_appcontext

@click.command(name="seed")
@with_appcontext
def seed():
    Burrito.query.delete()
    Order.query.delete()
    burrito1 = Burrito(name="Spicy Alsation", price=7.95)
    burrito2 = Burrito(name="Questionable Quorn", price=8.95)
    burrito3 = Burrito(name="Vegan Assault", price=6.95)

    db.session.add(burrito1)
    db.session.add(burrito2)
    db.session.add(burrito3)
    db.session.commit()

    order1 = Order()
    order2 = Order()
    order3 = Order()

    db.session.add(order1)
    db.session.add(order2)
    db.session.add(order3)
    db.session.commit()


