from flask import Flask, render_template
#ExtDeprecationWarning: Importing flask.ext.bootstrap is deprecated, use flask_bootstrap instead.
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def creat_app():
	app = Flask(__name__)
	app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:zhangtao@localhost/project'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	app.config['SECRET_KEY'] = '\xf8%\x9b\xd9\xb2a\xeam\xc96\xdf\x9dn\xc9\xfdH\xc8n\xff\xf3:\xf9\xb4\xac'

	bootstrap.init_app(app)
	db.init_app(app)
	login_manager.init_app(app)
	
	from .views.index import index
	app.register_blueprint(index, url_prefix='/app')

	from .auth import auth as auth_blueprint
	app.register_blueprint(auth_blueprint, url_prefix='/auth')

	@app.errorhandler(404)
	def page_not_found(e):
		return render_template('404.html')

	@app.errorhandler(500)
	def internal_server_error(e):
		return render_template('500.html')
	
	return app