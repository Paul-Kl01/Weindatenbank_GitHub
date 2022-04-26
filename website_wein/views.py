import random
from flask import Blueprint, redirect, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import *
import json

views = Blueprint('views', __name__)

@views.route('', methods=['GET', 'POST'])
@login_required
def home():
    weine = Wein.query.order_by(Wein.name).all()
    print(weine)
    wein = random.choice(weine)
    return render_template("home.html", user=current_user, wein=wein)

@views.route('/hinzufuegen', methods=['POST', 'GET'])
@login_required
def hinzufuegen():
    return render_template('hinzufuegen.html', user=current_user)

@views.route('/submit', methods=['POST', 'GET'])
@login_required
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        laden = request.form.get('laden')
        art = request.form.get('art')
        sorte = request.form.get('sorte')

        print(name, laden, art, sorte)

        if db.session.query(Wein).filter(Wein.name == name).count() == 0:
            data = Wein(name=name, laden=laden, art=art, sorte=sorte)
            db.session.add(data)
            db.session.commit()
            return redirect('/hinzufuegen')
        return render_template('hinzufuegen.html', user=current_user)
    else:
        return render_template('hinzufuegen.html', user=current_user, message='You have already submitted feedback')
