from flask import Blueprint, render_template, flash, redirect, url_for
from ..modules import Words, Translates
from .. import db
from flask_login import login_required

index = Blueprint('index', __name__)

@index.route('/index')
@login_required
def index_page():
	return '<h2>Hello</h2>'

@index.route('/words-list')
def query_all():
	word_dict = {}
	words_list = Words.query.all()
	for word in words_list:
		trans = Translates.query.filter_by(word_id=word.id).all()
		word_dict[word] = trans

	return render_template('index.html', words=word_dict)

@index.route('/delete/<int:id>')
def delete_word(id):	
	translates = Translates.query.filter_by(word_id=id).all()
	for translate in translates:
		db.session.delete(translate)

	word = Words.query.filter_by(id=id).first_or_404()
	db.session.delete(word)

	db.session.commit()
	flash('delete successfully!')
	return redirect(url_for('index.query_all'))

@index.route('/page-test')
def show_page():
	return render_template('page.html')
