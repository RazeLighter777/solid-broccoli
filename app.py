from flask import Flask, send_from_directory, render_template
from flask_autoindex import AutoIndexBlueprint
from flask import Blueprint

app = Flask(__name__,
	static_url_path='', 
	static_folder='static',
	template_folder='templates'
)
#add folder listing to the page
bp_ai = Blueprint('browse',__name__, static_folder='./static', template_folder='./templates')
ppath = "/mnt"
AutoIndexBlueprint(bp_ai, browse_root=ppath, template_context=dict(x='y'))
app.register_blueprint(bp_ai, url_prefix='/files')


@app.route('/')
def home():
	return render_template('home.html')

@app.route('/contact_us')
def contact_us():
	return render_template('contact_us.html')

@app.route('/manufacturing')
def manufacturing():
	return render_template('manufacturing.html')

@app.route('/solar_generation')
def solar_generation():
	return render_template('solar_generation.html')

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/admin')
def admin():
	return render_template('admin.html')

app.run(host='0.0.0.0', port=5000)
