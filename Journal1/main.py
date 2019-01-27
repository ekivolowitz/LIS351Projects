from flask import Flask, render_template, request
import json
from pprint import pprint
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
@app.route("/letters", methods=["POST"])
def letters():
    if request.method == 'POST':
        if 'myFile' not in request.files:
            return render_template("index.html")
        file = request.files['myFile']
        filename = "uploads/" + secure_filename(file.filename)
        file.save(filename)

        with open(filename, 'r') as f:
            chars = {}
            for char in f.read():
                if not char.isalpha():
                    continue
                char = char.lower()
                if char in chars.keys():
                    chars[char] += 1
                else:
                    chars[char] = 1
            return render_template("letters.html", counts = chars, keys = sorted(list(chars.keys())))

    return render_template("index.html")
@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="localhost", port=5000)