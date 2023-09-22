from flask import Flask, render_template, request, redirect
from flask import Blueprint
from app import db
from models.burrito_order import Burrito_order

burrito_order_blueprint = Blueprint("burrito_orders", __name__)

# this should contain the controller functions that handle requests to do with your "burrito_order(s)" class/table


