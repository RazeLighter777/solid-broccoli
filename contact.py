from flask import redirect, render_template, request, Blueprint, url_for, flash
from flask_login import LoginManager, login_required, logout_user, current_user, login_user
from werkzeug.utils import secure_filename
import os

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

bp = Blueprint('contact', __name__)

def allowed_file(filename):
	return True
	# return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def init_bp(app):
	@bp.route('/send', methods=['POST'])
	def sender():
		# check if the post request has the file part
		if 'file' not in request.files:
			flash('No file part')
			return redirect('/contact_us?code=0')
		file = request.files['file']
		# If the user does not select a file, the browser submits an
		# empty file without a filename.
		if file.filename == '':
			flash('No selected file')
			return redirect('/contact_us?code=0')
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return redirect('/contact_us?code=1')
		return redirect('/contact_us?code=0')

	def render_page(file, **kwargs):
		return render_template(file, user=current_user, **kwargs)