from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.order import Order
from models.burrito import Burrito
from app import db

burrito_blueprint = Blueprint("burritos", __name__)

@burrito_blueprint.route("/home")
def home():

    return render_template("/home.jinja")

@burrito_blueprint.route("/burritos")
def show_all_burritos():

    all_burritos = Burrito.query.all()
    return render_template("/burritos.jinja", burritos=all_burritos)
