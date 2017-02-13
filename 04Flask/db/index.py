# coding: utf8

from flask import Flask
from flask import render_template
from flask import g
from flask import request
from flask import redirect
from database import Database

app = Flask(__name__)


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
def start_page():
    return render_template('accueil.html')


@app.route('/liste')
def show_list():
    artists = get_db().get_artists()
    return render_template('artistes.html', artists=artists)


@app.route('/deux-listes')
def show_two_lists():
    artists = get_db().get_artists()
    albums = get_db().get_albums()
    return render_template('2listes.html', artists=artists, albums=albums)


@app.route('/vide')
def show_two_empty_lists():
    artists = []
    albums = []
    return render_template('2listes-vides.html', artists=artists, albums=albums)


@app.route('/formulaire')
def show_form():
    return render_template('form.html')


@app.route('/new', methods=['POST'])
def post_form():
    name = request.form['nom']
    if len(name) == 0:
        return render_template('form.html', erreur='Le nom est obligatoire')
    else:
        get_db().insert_artist(name)
        return redirect('/liste')