from . import db  # . ->means from this package
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):  # UserMixin -> nur für User nutzen
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
'''   
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
    nutzer_id = db.Column(db.Integer, db.ForeignKey('nutzer.nutzer_id'), primary_key=True, nullable=False)'''



