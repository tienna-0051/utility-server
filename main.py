import requests
import mmh3
import codecs
import subprocess
from flask import Flask, request, render_template
import warnings

warnings.filterwarnings("ignore")

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = '/tmp/'


@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')


@app.route('/favhash', methods=["GET", "POST"])
def favhash():
    output = ""
    error = ""
    if request.method == 'POST':
        if request.files.get('file'):
            file = request.files.get('file')
            favicon = codecs.encode(file.read(), "base64")
            output = f"http.favicon.hash:{mmh3.hash(favicon)}"
        else:
            response = requests.get(request.form.get("url"), verify=False)
            if response.status_code == 200 and "image" in response.headers['content-type']:
                favicon = codecs.encode(response.content, "base64")
                output = f"http.favicon.hash:{mmh3.hash(favicon)}"
            else:
                error = "Error in read image url"

    return render_template('favhash.html', output=output, error=error)


@app.route('/rce', methods=["GET", "POST"])
def rce():
    output = ""
    if request.method == 'POST':
        result = subprocess.run(request.form.get(
            "cmd"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = result.stdout.decode("utf-8")

    return render_template('rce.html', output=output)


# app.run()
