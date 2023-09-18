from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.order import Order
from models.burrito import Burrito
from models.customer import Customer
from app import db

customer_blueprint = Blueprint("customers", __name__)

@customer_blueprint.route("/customers")
def show_all_customers():
    all_customers = Customer.query.all()
    return render_template("/customers.jinja", customers=all_customers)

@customer_blueprint.route("/customers/<id>")
def show_one_customer(id):
    customer_to_show = Customer.query.get(id)
    customers_orders = customer_to_show.orders
    return render_template("/show_customer.jinja", customer=customer_to_show, orders=customers_orders)


@customer_blueprint.route("/customers", methods = ["POST"])
def add_customer():
    new_customer_name = request.form["customer_name"]
    new_phone_number = request.form["phone_number"]
    new_street_name = request.form["street_name"]

    customer_to_be_added = Customer(customer_name=new_customer_name, customer_phone_number=new_phone_number, customer_street_name=new_street_name)

    db.session.add(customer_to_be_added)
    db.session.commit()

    return redirect ("/customers")

@customer_blueprint.route("/customers/delete/<id>", methods=["POST"])
def delete_customer(id):
    customer_to_delete = Customer.query.get(id)
    if customer_to_delete:
        db.session.delete(customer_to_delete)
        db.session.commit()
        return redirect ("/customers")


@customer_blueprint.route("/order/<id>")
def show_single_order(id):
    order_to_show = Order.query.get(id)
    return redirect ("/create_order.jinja", order=order_to_show) 




