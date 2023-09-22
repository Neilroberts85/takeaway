from app import db
from models.burrito import Burrito
from models.burrito_order import Burrito_order

##########################
# example of extracting logic 
##########################

def handle_add_order_item(form_dict, order_id):

    burritos = Burrito.query.all()

    for burrito in burritos:
        quantity = form_dict.form.get(str(burrito.id))
        if int(quantity) > 0: 
            existing_burrito_order = Burrito_order.query.filter_by(burrito_id=burrito.id, order_id=order_id).first()
            if existing_burrito_order: 
                existing_burrito_order.quantity += int(quantity)
            else:
                burrito_order = Burrito_order(burrito_id=burrito.id, order_id=order_id, quantity=quantity)
                db.session.add(burrito_order)
    db.session.commit()