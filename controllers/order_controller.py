from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.burrito import Burrito
from models.burrito_order import Burrito_order
from models.order import Order
from app import db

order_blueprint = Blueprint("orders", __name__)

@order_blueprint.route("/orders")
def show_all_orders():
    all_orders = Order.query.all()
    return render_template("/orders.jinja", orders=all_orders)

@order_blueprint.route("/orders/<id>")
def show_order(id):
    order_to_show = Order.query.get(id)
    burritos = Burrito.query.all()
    return render_template("show_order.jinja", order=order_to_show, burritos=burritos)

@order_blueprint.route("/orders/<id>", methods=["POST"])
def add_to_order(id):
    burritos = Burrito.query.all()
    

    for burrito in burritos:
        quantity = request.form[str(burrito.id)]
        if int(quantity) > 0:
            burrito_order = Burrito_order(burrito_id=int(burrito.id), order_id=id, quantity=quantity)
            db.session.add(burrito_order)
            db.session.commit()

    id_for_path = id
    return redirect (f"/orders/{id_for_path}")
    




# @order_blueprint.route("/create_order", method=["POST"])
# def new_order():
#     burritos = Burrito.query.all()
#     orders = Order.query.all()
