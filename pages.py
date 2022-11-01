from flask import (Blueprint, request, render_template)
from flask_login import current_user

bp = Blueprint('pages', __name__)

@bp.route('/')
def home():
	return render_page('home.html')

@bp.route('/contact_us')
def contact_us():
	return render_page('contact_us.html')

@bp.route('/manufacturing')
def manufacturing():
	return render_page('manufacturing.html')

@bp.route('/solar_generation')
def solar_generation():
	return render_page('solar_generation.html')

@bp.route('/login', methods = ['GET'])
def login_page():
	return render_page('login.html', didLoginFail=(request.args.get('error') == '1'))

def render_page(file, **kwargs):
	return render_template(file, user=current_user, **kwargs)