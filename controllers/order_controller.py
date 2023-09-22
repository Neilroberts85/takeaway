from flask import Flask, render_template, request, redirect, url_for
from flask import Blueprint
from models.burrito import Burrito
from models.burrito_order import Burrito_order
from models.order import Order
from models.customer import Customer
from services.burrito_orders_services import handle_add_order_item
from app import db

order_blueprint = Blueprint("orders", __name__)

# we can consider extracting out logic and extra verbosity from our controller functions into a separate file, we care more about _what_ are code is doing as opposed to _how_ its doing it. 
# see bottom of file for example
# this has the following benefits ..

# 1. Separation of concerns
# One of the core principles of software engineering is the separation of concerns. By moving business logic out of controllers and into separate components, you ensure that each component has a single responsibility. Controllers should primarily handle user input and orchestrate the flow of data, while logic related to data manipulation, validation, and business rules should be handled by other parts of the application.
# 2. Code Reusability (keeps us DRY)
# Extracting logic into separate modules or classes makes it more reusable. You can use the same logic in multiple controllers or even in different parts of your application. This reduces code duplication and leads to a more maintainable codebase.
# 3. Scalable 
# As your application grows, you may need to change or extend its functionality, if we have to do the same action several times, it helps if we have the logic to do that action central to one place if we suddenly need to change how we are doing that action we now need to just change the code in one place as apposed to every place we where doing that action.
# 4. Readability 
# Controllers are typically responsible for managing the flow of requests and responses. When logic is mixed with controller code, it can make controllers bulky and less readable. Extracting logic into separate files/folders leads to cleaner, more focused, and more readable code. This improves the overall maintainability of the application. 

@order_blueprint.route("/orders", methods=["POST"])
def create_order():
    # customers = Customer.query.all()
    
    new_customer_id = request.form["customers"]
    

    order_to_be_added = Order(customer_id=new_customer_id)

    db.session.add(order_to_be_added)
    db.session.commit()

    return redirect("/orders")

@order_blueprint.route("/customers/<id>/create_order")
def create_order_from_cust(id):

    order_to_be_added = Order(customer_id=id)

    db.session.add(order_to_be_added)
    db.session.commit()

    return redirect(f"/customers/{id}")




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
# route should be "/orders/<id>/burrito_order" as we are creating a new "burrito_order" 
# the POST route for "/orders/<id>" should be saved for editing a order
# I did an example of extracting the logic out of this function to make it neater. 
@order_blueprint.route("/orders/<id>", methods=["POST"])
def add_burritos_to_order(id):
    
        burritos = Burrito.query.all()

        for burrito in burritos:
            quantity = request.form.get(str(burrito.id))
            if quantity and int(quantity) > 0: # I think this 'and' is redundant as we are checking in the first part if "quantity" is truthy which as it's a not empty string will always be True
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



##########################
# example of extracting logic 
##########################

@order_blueprint.route("/orders/<id>", methods=["POST"])
def add_burritos_to_order(id):
        handle_add_order_item(request.form, id)
        return redirect (f"/orders/{id}")


# this leaves us with code that is more 'self documenting' e.g it looks like natural language and is easier to read. It keeps our controller adhering more to the single responsibility princable (it's code is responsable for handling requests, and sending responses.)



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
    
