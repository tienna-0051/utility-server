import requests
import mmh3
import codecs
from flask import Flask, request, render_template
import warnings

warnings.filterwarnings("ignore")

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')


@app.route('/favhash', methods=["GET", "POST"])
def favhash():
    output = ""
    if request.method == 'POST':
        response = requests.get(request.form.get("url"), verify=False)
        favicon = codecs.encode(response.content, "base64")
        output = f"http.favicon.hash:{mmh3.hash(favicon)}"

    return render_template('favhash.html', output=output)

# app.run()
