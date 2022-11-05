from flask import redirect, render_template, request, Blueprint, Response
from flask_login import LoginManager, login_required, logout_user, current_user, login_user
import requests
import socketio

bp = Blueprint('solar', __name__)

sio = socketio.Client(logger=False, engineio_logger=False)

solarArrayData = [{},{},{},{},{},{}];

@sio.event
def connect():
	print("I'm connected!")

@sio.event
def connect_error(data):
	print("The connection failed!")

@sio.event
def disconnect():
	print("I'm disconnected!")

sio.connect('http://10.0.122.76:1880', namespaces=['/react_ArrayOV'], socketio_path='uibuilder/vendor/socket.io/')

@sio.event(namespace='/react_ArrayOV')
def uiBuilder(data):
	if data['topic'].startswith('array'):
		solarIndex = int(data['topic'][5]) - 1
		solarProp = data['topic'][7:]
		solarArrayData[solarIndex][solarProp] = data['payload']

def init_bp(app):
	@bp.route('/')
	def home():
		return render_template('solar.html');

	@bp.route('/api')
	def api():
		return {
			'solarData': solarArrayData,
			'trackerTiltDegree': 220,
			'azimuthAngle': 130
		}