# coding: utf8


from flask import Flask
from flask import render_template
from flask import g
from database import Database

app = Flask(__name__, static_url_path="", static_folder="static")


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Database()
    return g._database


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.disconnect()


@app.route('/')
def form():
    pays = get_db().get_pays()
    return render_template('form.html', pays=pays)


@app.route('/provinces/<pays_id>')
def provinces(pays_id):
    provinces = get_db().get_provinces(pays_id)
    return render_template('provinces.html', provinces=provinces)


@app.route('/villes/<province_id>')
def villes(province_id):
    villes = get_db().get_villes(province_id)
    return render_template('villes.html', villes=villes)