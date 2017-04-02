from werkzeug.security import generate_password_hash, check_password_hash

from . import db
from flask_login import UserMixin
from . import login_manager

class Words(db.Model):
	"""docstring for Words"""
	__tablename__ = 'words'
	id = db.Column(db.Integer, primary_key=True)
	word = db.Column(db.String(50))
	trans = db.relationship('Translates', backref='words')

class Translates(db.Model):
	"""docstring for Translates"""
	id = db.Column(db.Integer, primary_key=True)
	Translate = db.Column(db.String(50))
	word_id = db.Column(db.Integer, db.ForeignKey('words.id'))

class User(UserMixin, db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(64), unique=True, index=True)
	username = db.Column(db.String(64), unique=True, index=True)
	password_hash = db.Column(db.String(128))

	def __init__(self, email, username, password):
		self.email = email
		self.username = username
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))	