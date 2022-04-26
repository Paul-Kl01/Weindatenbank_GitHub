import random
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import *
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    weine = Wein.query.order_by(Wein.name).all()
    print(weine)
    wein = random.choice(weine)
    return render_template("home.html", user=current_user, wein=wein)

# @views.route('/liste', methods=['GET'])
# @login_required
# def getWein():
#     weine = Wein.query.order_by(Wein.name).all()
#     return render_template('liste.html', weine=weine)