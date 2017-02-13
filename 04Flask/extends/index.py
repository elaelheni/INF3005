# coding: utf8

from flask import Flask
from flask import render_template

app = Flask(__name__, static_url_path="", static_folder="static")


@app.route('/')
def page_accueil():
    return render_template('accueil.html')


@app.route('/inf3005/')
def page_prog_web_avancee():
    return render_template('inf3005.html')
