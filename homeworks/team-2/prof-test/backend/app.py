import os
from flask import Flask
from flask import render_template, request, redirect
from models import db_q, db_save, db_delete
import config
import sys
sys.path.append("./models")
from base import db

app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)

@app.route("/")
def index():
    q = db_q(1)
    return render_template("index.html", q=q)

@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/save", methods=["POST"])
def save():
    q = request.form['question']
    t = request.form['type']
    db_save(q=q, t=t)
    return redirect("/")

@app.route("/del/<id>")
def delete(id):
    db_delete(id)
    return redirect("/")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
