from flask import Flask, send_from_directory, render_template

app = Flask(__name__,
    static_url_path='', 
    static_folder='static',
    template_folder='templates'
)

@app.route('/')
def home():
    return render_template('index.html')

app.run(host='0.0.0.0', port=5000)
