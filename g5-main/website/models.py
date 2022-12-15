from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy.sql.schema import ForeignKeyConstraint , UniqueConstraint
#look up flask.alchemy
#one to many

#Player
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# this class holds the database that is connected to the user which is logged in 
class User(db.Model, UserMixin): #layout or blueprint of class
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
    players = db.relationship('Player')

# this class holds the blueprint of the player which you are updating 
class Player(db.Model): 
    player_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    id = db.Column(db.Integer)
    name = db.Column(db.String(150))
    date = db.Column(db.String(150))
    coursename = db.Column(db.String(150)) 
    holes = db.relationship('Holes')

# this class holds the database structure for the inputted stats 
class Holes(db.Model):
    holes_id = db.Column(db.Integer, db.ForeignKey('player.id'), primary_key=True)
    pars = db.Column(db.String(150))
    scores = db.Column(db.Integer)
    fairways= db.Column(db.String(150))
    girs = db.Column(db.String(150))
    approachds = db.Column(db.Integer)
    uds = db.Column(db.String(150))
    suds = db.Column(db.String(150))
    putts = db.Column(db.Integer)
    p2hs = db.Column(db.Integer)

    id = db.Column(db.Integer, primary_key=True)
