from flask import redirect, render_template, request, Blueprint, Response
from flask_login import LoginManager, login_required, logout_user, current_user, login_user
import requests

bp = Blueprint('solar', __name__)

def init_bp(app):
	# @bp.before_request
	# @login_required
	# def login_required_for_all_request():    
	# 	pass

	@bp.route('/')
	def home():
		return render_template('solar.html')
	
	@bp.route('/<path:path>',methods=['GET','POST','DELETE'])
	def proxy(path):
		SITE_NAME = 'http://10.0.122.76:1880/react_ArrayOV/'
		print(f'{SITE_NAME}{path}')
		if request.method=='GET':
			resp = requests.get(f'{SITE_NAME}{path}')
			excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
			headers = [(name, value) for (name, value) in  resp.raw.headers.items() if name.lower() not in excluded_headers]
			response = Response(resp.content, resp.status_code, headers)
			return response
		elif request.method=='POST':
			resp = requests.post(f'{SITE_NAME}{path}',json=request.get_json())
			excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
			headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
			response = Response(resp.content, resp.status_code, headers)
			return response
		elif request.method=='DELETE':
			resp = requests.delete(f'{SITE_NAME}{path}').content
			response = Response(resp.content, resp.status_code, headers)
			return response