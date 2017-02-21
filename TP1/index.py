# coding: utf8


from flask import Flask
from flask import render_template
from flask import g
from flask import request
from flask import redirect
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
def start_page():
    publications = get_db().get_5_last_publications()
    ids = get_db().get_id_article()
    titres = get_db().get_titre_article()
    identifiants = get_db().get_identifiant_article()
    auteurs = get_db().get_auteur_article()
    dates = get_db().get_date_publication_article()
    paragraphes = get_db().get_paragraphe_article()
    return render_template('accueil.html', publications=publications, ids=ids, titres=titres, identifiants=identifiants, auteurs=auteurs, dates=dates, paragraphes=paragraphes)
