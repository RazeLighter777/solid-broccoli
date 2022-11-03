from flask import redirect, render_template, request, Blueprint
from flask_login import LoginManager, login_required, logout_user, current_user, login_user
import email
import imaplib
import pprint
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

imap_host = os.environ.get('IMAP_HOST')
imap_user = os.environ.get('IMAP_USER')
imap_pass = os.environ.get('IMAP_PASS')

# connect to host
imap = imaplib.IMAP4(imap_host)
print(imap)

## login to server
imap.login(imap_user, imap_pass)

imap.select('Inbox')

bp = Blueprint('mail', __name__)

def init_bp(app):
	@bp.before_request
	@login_required
	def login_required_for_all_request():    
		pass
	
	@bp.route('/')
	def root():
		data, messages = imap.search('UTF-8', "ALL")
		print(messages)

		emails = []

		for message in messages[0].split():
			typ, data = imap.fetch(message, "(UID BODY[HEADER] BODY[TEXT])")

			header = data[0][1].decode("utf-8").split('\r\n');
			author = header[0][len('Return-Path: '):]
			subject = header[3][len('Subject: '):]

			emails.append([author, subject, data[1][1].decode("utf-8")])

		print(emails)

		return render_page('mail.html', messages=emails);

def render_page(file, **kwargs):
	return render_template(file, user=current_user, **kwargs)