from flask import Flask, render_template, request, redirect
from flask import Blueprint
from app import db
from models.burrito_order import Burrito_order

burrito_order_blueprint = Blueprint("burrito_orders", __name__)


