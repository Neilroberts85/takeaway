from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://neilroberts@localhost:5432/tasks_app"
db = SQLAlchemy(app)

from models.burrito import Burrito
from models.burrito_order import Customer
from models.order import Order

migrate = Migrate(app, db)