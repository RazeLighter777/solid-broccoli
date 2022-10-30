from flask import Flask, send_from_directory, render_template

app = Flask(__name__,
	static_url_path='', 
	static_folder='static',
	template_folder='templates'
)

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

app.run(host='0.0.0.0', port=5000)
