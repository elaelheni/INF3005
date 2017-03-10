# coding: utf8


from flask import Flask
from flask import render_template
from flask import g
from flask import make_response
from flask import request
from database import Database

app = Flask(__name__)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Database()
    return  g._database


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.disconnect()


@app.route('/')
def start_page():
    artists = get_db().get_artists()
    last_id = request.cookies.get('last')
    last_artist = None
    if last_id is not None:
        last_artist = get_db().get_artist(last_id)
    return render_template('accueil.html', artists=artists, last=last_artist)

# 410 -> Existait avant, n'existe pu maintenant
# 404 -> N'existe pas
# 401 -> Pas d'authtification
# 200 -> Pas d'erreur, Ok
# 400 -> Manque de quoi dans le formulaire

@app.route('/artiste/<identifier>')
def artist_page(identifier):
    artist = get_db().get_artist(identifier)
    if artist is None:
        return render_template('404.html'), 404
    else:
        response = make_response(render_template('artiste.html', artist=artist)) 
		# ('22/templates/artiste.html', article=article)) SI ON VEUT METTRE artiste.html dans un sous dossier
        response.set_cookie('last', identifier)
        return response
