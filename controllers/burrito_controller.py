from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.order import Order
from models.burrito import Burrito
from app import db

burrito_blueprint = Blueprint("burritos", __name__)

@burrito_blueprint.route("/home")
def home():
    return render_template("/home.jinja")

@burrito_blueprint.route("/menu")
def show_all_burritos():
    all_burritos = Burrito.query.all()
    return render_template("/burritos.jinja", burritos=all_burritos)

@burrito_blueprint.route("/menu/<id>")
def show_one_burrito(id):
    burrito_to_show = Burrito.query.all(id)
    return render_template("/show_one_burrito.jinja", burrito=burrito_to_show)

@burrito_blueprint.route("/menu", methods = ["POST"])
def add_burrito():
    burrito_name = request.form["name"]
    burrito_price = request.form["price"]
    
    burrito_to_be_added = Burrito(name=burrito_name, price=burrito_price)

    db.session.add(burrito_to_be_added)
    db.session.commit()

    return redirect ("/menu")

@burrito_blueprint.route("/burritos/delete/<id>", methods=["POST"])
def delete_burrito(id):
    burrito_to_delete = Burrito.query.get(id)
    if burrito_to_delete:
        db.session.delete(burrito_to_delete)
        db.session.commit()
        return redirect ("/menu")


