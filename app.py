# Imports
from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

# App initialisieren
app = Flask(__name__)

# Environment bestimmen
ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/weindatenbank'
else:
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Datenbank initialisieren
db = SQLAlchemy(app)

# ---
# Datenbank Model/Schema erstellen
# ---


class Wein(db.Model):
    __tablename__ = 'wein'
    wein_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    laden = db.Column(db.String(200))
    art = db.Column(db.String(200))
    sorte = db.Column(db.String(200))

    def __init__(self, name, laden, art, sorte):
        self.name = name
        self.laden = laden
        self.art = art
        self.sorte = sorte


# Routing erstellen
@app.route('/')
def index():
    weine = Wein.query.order_by(Wein.name).all()
    print(weine)
    wein = random.choice(weine)
    return render_template('index.html', wein = wein)


@app.route('/submit', methods=['POST','GET'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        laden = request.form['laden']
        art = request.form['art']
        sorte = request.form['sorte']

        print(name, laden, art, sorte)

        if db.session.query(Wein).filter(Wein.name == name).count() == 0:
            data = Wein(name, laden, art, sorte)
            db.session.add(data)
            db.session.commit()
            return redirect('/submit')
        return render_template('hinzufuegen.html', message='You have already submitted feedback')
    else: 
        # weine = Wein.query.order_by(Wein.name).all()
        # print("Test")
        return render_template('hinzufuegen.html' )

@app.route('/liste', methods=['GET'])
def getWein():
    weine = Wein.query.order_by(Wein.name).all()
    return render_template('liste.html', weine=weine )

@app.route('/hinzufuegen', methods=['GET'])
def start():
    return render_template('hinzufuegen.html')


@app.route('/search', methods=['POST'])
def searchDB():
    print("POST")
    wein = request.form['name']
    print(wein)
    weine = Wein.query.filter_by(name=wein).all()
    return render_template('liste.html', weine=weine )     

# App starten
if __name__ == '__main__':
    app.run()
