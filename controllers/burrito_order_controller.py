from flask import Flask, render_template, request, redirect
from flask import Blueprint
from app import db

burrito_order_blueprint = Blueprint("burrito_orders", __name__)