from myapp import creat_app
#ExtDeprecationWarning: Importing flask.ext.script is deprecated, use flask_script instead.
from flask_script import Manager, Command

from tranlate import shell

app = creat_app()
manager = Manager(app)

@manager.command
def translate():
	"""translate words to chinese"""
	shell()

if __name__ == '__main__':
	manager.run()