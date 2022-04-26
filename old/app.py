# Imports
from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

# Zufallgenerator initialisieren
random.seed()

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
    bewertungen = db.relationship('Bewertung')
    gerichte = db.relationship('PassendeGerichte')

    def __init__(self, name, laden, art, sorte):
        self.name = name
        self.laden = laden
        self.art = art
        self.sorte = sorte


class Nutzer(db.Model):
    __tablename__ = 'nutzer'
    nutzer_id = db.Column(db.Integer, primary_key=True)
    nutzername = db.Column(db.String(200))  # TODO Nutzername unique machen
    email = db.Column(db.String(200))
    passwort = db.Column(db.String(200))
    bewertungen = db.relationship('Bewertung')

    def __init__(self, nutzername, email, passwort):
        self.nutzername = nutzername
        self.email = email
        self.passwort = passwort


class Gericht(db.Model):
    __tabelname__ = 'gericht'
    gericht_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    gerichte = db.relationship('PassendeGerichte')

    def __init__(self, name):
        self.name = name


class PassendeGerichte(db.Model):
    __tablename__ = 'passendeGerichte'
    wein_id = db.Column(db.Integer, db.ForeignKey('wein.wein_id'), primary_key=True, nullable=False)
    gericht_id = db.Column(db.Integer, db.ForeignKey('gericht.gericht_id'), primary_key=True, nullable=False)


class Bewertung(db.Model):
    __tablename__ = 'bewertung'
    wein_id = db.Column(db.Integer, db.ForeignKey('wein.wein_id'), primary_key=True, nullable=False)
    nutzer_id = db.Column(db.Integer, db.ForeignKey('nutzer.nutzer_id'), primary_key=True, nullable=False)


# Routing erstellen
@app.route('/')
def index():
    weine = Wein.query.order_by(Wein.name).all()
    print(weine)
    wein = random.choice(weine)
    return render_template('index.html', wein=wein)


# TODO besser benennen der requests

@app.route('/submit', methods=['POST', 'GET'])
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
        return render_template('hinzufuegen.html')


@app.route('/liste', methods=['GET'])
def getWein():
    weine = Wein.query.order_by(Wein.name).all()
    return render_template('liste.html', weine=weine)


@app.route('/hinzufuegen', methods=['GET'])
def start():
    return render_template('hinzufuegen.html')


@app.route('/search', methods=['POST'])
def searchDB():
    print("POST")
    wein = request.form['name']
    print(wein)
    weine = Wein.query.filter_by(name=wein).all()
    return render_template('liste.html', weine=weine)

# App starten
if __name__ == '__main__':
    db.create_all()
    app.run()
