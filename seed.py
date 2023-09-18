from app import db
from models.burrito import Burrito
from models.order import Order
from models.burrito_order import Burrito_order
from models.customer import Customer
import click 

from flask.cli import with_appcontext

@click.command(name="seed")
@with_appcontext
def seed():
    Burrito_order.query.delete()
    Order.query.delete()
    Burrito.query.delete()
    Customer.query.delete()
    

    burrito1 = Burrito(name="Spicy Alsation", price=7.95)
    burrito2 = Burrito(name="Questionable Quorn", price=8.95)
    burrito3 = Burrito(name="Vegan Assault", price=6.95)

    db.session.add(burrito1)
    db.session.add(burrito2)
    db.session.add(burrito3)

    customer1 = Customer(customer_name="Hungry Horatio", customer_phone_number="07756748576", customer_street_name="Letsby Avenue")
    customer2 = Customer(customer_name="Starvin' Marvin", customer_phone_number="07070707070", customer_street_name="Sunset Strip")
    customer3 = Customer(customer_name="Jumpin' Jack", customer_phone_number="07756748573", customer_street_name="Castle Terrace")

    db.session.add(customer1)
    db.session.add(customer2)
    db.session.add(customer3)

    db.session.commit()

    order1 = Order(customer_id=customer1.id)
    order2 = Order(customer_id=customer2.id)
    order3 = Order(customer_id=customer3.id)

    db.session.add(order1)
    db.session.add(order2)
    db.session.add(order3)
    
    db.session.commit()

    burrito_order1 = Burrito_order(burrito_id=burrito1.id, order_id=order1.id)
    burrito_order2 = Burrito_order(burrito_id=burrito2.id, order_id=order2.id)
    burrito_order3 = Burrito_order(burrito_id=burrito3.id, order_id=order3.id)

    db.session.add(burrito_order1)
    db.session.add(burrito_order2)
    db.session.add(burrito_order3)

    db.session.commit()

if __name__ == '__main__':
    seed()