from flask import Flask, g, redirect, send_from_directory, render_template, url_for
from flask_autoindex import AutoIndexBlueprint
from flask import Blueprint
from flask_login import LoginManager, login_required, logout_user, current_user, login_user
import os
from flask import request

app = Flask(__name__,
	static_url_path='', 
	static_folder='static',
	template_folder='templates'
)
app.secret_key = os.urandom(24)


#add folder listing to the page
bp_ai = Blueprint('browse',__name__, static_folder='./static', template_folder='./templates')
ppath = "/mnt"
AutoIndexBlueprint(bp_ai, browse_root=ppath, template_context=dict(x='y'))
app.register_blueprint(bp_ai, url_prefix='/files')

#User management
class User:
    name = ""
    def __init__(self, name):
        self.name = name
    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return self.name
    def to_json(self):
        return {"name": self.name}
    def admin(self):
        return self.name == "admin"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
@login_manager.user_loader
def load_user(user_id):
	return User(user_id)


@app.route('/login', methods = ['POST'])
def login():
	username = request.form['username']
	password = request.form['password']
	if username == 'admin' and password == 'admin':
		user = User(username)
		login_user(user)
		return redirect('/')
	else:
		return redirect('/login?error=1')

@app.route('/logout')
def logout():
	logout_user()
	return redirect('/')

@app.route('/')
def home():
	return render_page('home.html')

@app.route('/contact_us')
def contact_us():
	return render_page('contact_us.html')

@app.route('/manufacturing')
def manufacturing():
	return render_page('manufacturing.html')

@app.route('/solar_generation')
def solar_generation():
	return render_page('solar_generation.html')

@app.route('/login', methods = ['GET'])
def login_page():
	return render_page('login.html', didLoginFail=(request.args.get('error') == '1'))

@app.route('/admin')
@login_required
def admin():
	return render_page('admin.html')

def render_page(file, **kwargs):
	return render_template(file, user=current_user, **kwargs)

if __name__ == "__name__":
	app.run(host='0.0.0.0', port=5000)
