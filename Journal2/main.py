
from flask import Flask, render_template, request
import json
from pprint import pprint
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
@app.route("/size", methods=["POST"])
def letters():
    if request.method == 'POST':
        if 'myFile' not in request.files:
            return render_template("index.html")
        file = request.files['myFile']
        filename = "uploads/" + secure_filename(file.filename)
        file.save(filename)

        with open(filename, 'r') as f:
            stats = os.stat(filename)
            kb = stats.st_size / (2 ** 10)
            mb = stats.st_size / (2 ** 20)
            gb = stats.st_size / (2 ** 30)
            tb = stats.st_size / (2 ** 40)
            return render_template("letters.html", size=stats.st_size, kb=kb, mb=mb, gb=gb, tb=tb)

    return render_template("index.html")
@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="localhost", port=5000)