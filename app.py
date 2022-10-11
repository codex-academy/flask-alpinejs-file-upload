from flask import Flask, request, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

url_for('static', filename='index.html')

@app.route('/api/upload', methods=['GET', 'POST'])
def upload_file():

    if request.method == 'POST':
        file = request.files['image']
        file_name = secure_filename(file.filename)
        print (file_name)
        file.save(f"./{secure_filename(file_name)}")

    return 'ok'

        # f.save('./uploaded.file')
