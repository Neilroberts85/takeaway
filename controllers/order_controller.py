from flask import Flask, render_template, request, redirect, url_for
from flask import Blueprint
from models.burrito import Burrito
from models.burrito_order import Burrito_order
from models.order import Order
from models.customer import Customer
from app import db

order_blueprint = Blueprint("orders", __name__)

@order_blueprint.route("/orders", methods=["POST"])
def create_order():
    customers = Customer.query.all()
    
    new_customer_id = request.form["customers"]
    

    order_to_be_added = Order(customer_id=new_customer_id)

    db.session.add(order_to_be_added)
    db.session.commit()

    return redirect("/orders")





@order_blueprint.route("/orders")
def show_all_orders():
    all_orders = Order.query.all()
    customers = Customer.query.all()
    return render_template("/orders.jinja", orders=all_orders, customers=customers)

@order_blueprint.route("/orders/<id>")
def show_order(id):
    order_to_show = Order.query.get(id)
    burritos = Burrito.query.all()
    return render_template("show_order.jinja", order=order_to_show, burritos=burritos)

@order_blueprint.route("/orders/<id>", methods=["POST"])
def add_burritos_to_order(id):
    
        burritos = Burrito.query.all()
        for burrito in burritos:
            quantity = request.form.get(str(burrito.id))
            if quantity and int(quantity) > 0:
                existing_burrito_order = Burrito_order.query.filter_by(burrito_id=burrito.id, order_id=id).first()
                if existing_burrito_order:
                    existing_burrito_order.quantity += int(quantity)
                else:
                    burrito_order = Burrito_order(burrito_id=burrito.id, order_id=id, quantity=quantity)
                    db.session.add(burrito_order)

        db.session.commit()
        return redirect (f"/orders/{id}")

@order_blueprint.route("/burrito_order/delete/<id>", methods=["POST"])
def delete_burrito_order(id):
    
    burrito_order_to_delete = Burrito_order.query.get(id)
    order_page_id = burrito_order_to_delete.order_id
    if burrito_order_to_delete:
        db.session.delete(burrito_order_to_delete)
        db.session.commit()

    
    return redirect (f"/orders/{order_page_id}")

@order_blueprint.route("/orders/delete/<id>", methods=["POST"])
def delete_order(id):
    order_to_delete = Order.query.get(id)
    if order_to_delete:
        db.session.delete(order_to_delete)
        db.session.commit()
        return redirect ("/orders")





# def add_to_order(id):
#     burritos = Burrito.query.all()
    

#     for burrito in burritos:
#         quantity = request.form[str(burrito.id)]
#         if int(quantity) > 0:
#             burrito_order = Burrito_order(burrito_id=int(burrito.id), order_id=id, quantity=quantity)
#             db.session.add(burrito_order)
#             db.session.commit()

#     id_for_path = id
#     return redirect (f"/orders/{id_for_path}")
    
