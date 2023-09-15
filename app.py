from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://neilroberts@localhost:5432/takeaway"
db = SQLAlchemy(app)

from models.burrito import Burrito
from models.burrito_order import Burrito_order
from models.order import Order

migrate = Migrate(app, db)
from seed import seed
app.cli.add_command(seed)

from controllers.burrito_controller import burrito_blueprint
from controllers.order_controller import order_blueprint
from controllers.burrito_order_controller import burrito_order_blueprint

app.register_blueprint(burrito_blueprint)
app.register_blueprint(order_blueprint)
app.register_blueprint(burrito_order_blueprint)

