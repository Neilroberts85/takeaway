from flask import Flask, render_template, request, redirect
from flask import Blueprint
from app import db

order_blueprint = Blueprint("orders", __name__)