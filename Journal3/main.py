from flask import Flask, render_template, request, g
import json
from pprint import pprint
import os
from werkzeug.utils import secure_filename
import sqlite3

DATABASE = "test.db"

def get_database():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db
def close():
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()
        
app = Flask(__name__)
@app.route("/login", methods=["POST"])
def letters():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username is not None and password is not None:    
            db = get_database()
            sqlQuery = "SELECT COUNT(*) FROM USERS WHERE username='" + username + "' AND pwd='" + password +"'"
            cursor = db.execute(sqlQuery)
            ret_value = cursor.fetchall()
            cursor.close()
            count = ret_value[0][0]
            if count > 0:
                return render_template('home.html', username=username)
    return render_template("index.html")
        
@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="localhost", port=5000)