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