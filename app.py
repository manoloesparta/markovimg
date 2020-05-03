import os
from PIL import Image
from markov import Markov
from werkzeug.utils import secure_filename
from flask import Flask, request, render_template, redirect, url_for, send_file

UPLOAD_FOLDER = 'files/'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
FINAL_IMG = os.path.join(app.config['UPLOAD_FOLDER'], 'tmp.jpg')

if not os.path.exists('files'):
    os.mkdir('files')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file_allowed(file.filename):
            file.save(FINAL_IMG)
            return redirect(url_for('view'))
    return 'No get requests here'

@app.route('/view', methods=['GET'])
def view():
    Image.open(FINAL_IMG).convert('RGB').save(FINAL_IMG)
    m = Markov(FINAL_IMG)
    m.create_chain()
    m.generate_image(FINAL_IMG)
    return send_file(FINAL_IMG)

def file_allowed(filename):
    ext = filename.split('.')[-1]
    return ext in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
