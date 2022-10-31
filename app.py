from flask import Flask, g, redirect, send_from_directory, render_template, url_for, request, Blueprint
from flask_autoindex import AutoIndexBlueprint
from flask_login import LoginManager, login_required, logout_user, current_user, login_user

import os

# Routes
import pages
import auth
import mail

app = Flask(__name__,
	static_url_path='', 
	static_folder='static',
	template_folder='templates'
)
app.secret_key = os.urandom(24)

auth.init_bp(app)
mail.init_bp(app)

#add folder listing to the page
bp_ai = Blueprint('browse', __name__, static_folder='./static', template_folder='./templates')
ppath = "/mnt"
AutoIndexBlueprint(bp_ai, browse_root=ppath, template_context=dict(x='y'))
app.register_blueprint(bp_ai, url_prefix='/files')
app.register_blueprint(pages.bp, url_prefix='/')
app.register_blueprint(auth.bp, url_prefix='/')
app.register_blueprint(mail.bp, url_prefix='/mail')


if __name__ == "__name__":
	app.run(host='0.0.0.0', port=5000)
