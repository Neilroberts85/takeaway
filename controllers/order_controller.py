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
def show_one_order(id):
    one_order = Order.query.all(id)
    return render_template("/show_one_burrito.jinja", order=one_order)

@order_blueprint.route("/orders", methods=["Post"])
def create_customer():
    new_customer_name = request.form["customer_name"]
    new_phone_number = request.form["phone_number"]
    new_street_name = request.form["street_name"]

    customer_to_be_added = Order(customer_name=new_customer_name, customer_phone_number=new_phone_number, customer_street_name=new_street_name)

    db.session.add(customer_to_be_added)
    db.session.commit()

    return redirect ("/orders")