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
    
