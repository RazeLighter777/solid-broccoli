from flask import redirect, render_template, request, Blueprint
from flask_login import LoginManager, login_required, logout_user, current_user, login_user

bp = Blueprint('auth', __name__)

# User management
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

def init_bp(app):
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

	@app.route('/admin')
	@login_required
	def admin():
		return render_page('admin.html')

	def render_page(file, **kwargs):
		return render_template(file, user=current_user, **kwargs)