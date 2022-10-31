from flask import redirect, render_template, request, Blueprint
from flask_login import LoginManager, login_required, logout_user, current_user, login_user

bp = Blueprint('mail', __name__)

def init_bp(app):
	@bp.route('/')
	def root():
		return "Mail Route!"