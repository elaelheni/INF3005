# coding: utf8

import datetime
from flask import Flask
from flask import render_template
from flask import g
from flask import request
from flask import redirect
from database import Database
from flask import make_response
from flask import request
import sys
reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__, static_url_path="", static_folder="static")


class ErreurDate(Exception):
    def __init__(self, path, msg):
        self.path = path
        self.msg = msg

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
    return render_template('accueil.html', publications=publications)


@app.route('/admin')
def admin_page():
    articles = get_db().get_all_article()
    return render_template('admin.html', articles=articles)


@app.route('/recherche', methods=['POST'])
def recherche_page():
    rechercher = request.form['rechercher']
    like_recher = '%%%s%%' % rechercher
    articles = get_db().get_search_articles(like_recher)
    return render_template('recherche.html', articles=articles, rechercher=rechercher)


@app.route('/admin-modifier/<ident>')
def admin_edit_page(ident):
    article = get_db().get_article(ident)
    return render_template('admin-modifier.html', article=article)


@app.route('/admin-form-modifier', methods=['POST'])
def admin_edit_form():
    articles = get_db().get_all_article()
    identifier = request.form['identifier']
    titre = request.form['titre']
    paragraphe = request.form['paragraphe']
    if len(titre) == 0:
        return render_template('admin-form.html', erreur='Le titre est obligatoire')
    else:
        get_db().uptade_article(identifier, titre, paragraphe)
        succes = "L'article %s à été modifié avec succes" % titre
        #return render_template('admin.html', articles=articles, succes=succes)
        return redirect('/admin')


@app.route('/article/<ident>')
def article_page(ident):
    article = get_db().get_article(ident)
    if article is None:
        return render_template('404.html'), 404
    else:
        return render_template('article.html', article=article)


@app.route('/article')
def article_main():
    return render_template('404.html'), 404


@app.route('/article/')
def article_main2():
    return render_template('404.html'), 404


@app.route('/admin-form')
def admin_add_form():
    return render_template('admin-form.html')


@app.route('/admin-form-new', methods=['POST'])
def admin_post_form():
    #articles = get_db().get_all_article()
    titre = request.form['titre']
    identifiant = request.form['identifiant']
    auteur = request.form['auteur']
    date_publication = request.form['date_publication']
    paragraphe = request.form['paragraphe']

    titre_val = validate_name(titre, 0, 100, 'Le titre est obligatoire', 'Le titre est trop long')
    ident_val = validate_name(identifiant, 0, 50, "L'identifiant est obligatoire", "L'identifiant est trop long")
    auteur_val = validate_name(auteur, 0, 100, "Le nom de l'auteur est obligatoire", "Le nom de l'auteur est trop long")
    date_val = validate_date(date_publication)
    paragraphe_val = validate_name(paragraphe, 0, 500, "Un paragraphe est obligatoire", "Le paragraphe est trop long")

    if titre_val != "" or ident_val != "" or auteur_val != "" or paragraphe_val != "" or date_val != "":
        return render_template('admin-form.html',
                               erreur_titre=titre_val,
                               erreur_ident=ident_val,
                               erreur_auteur=auteur_val,
                               erreur_date=date_val,
                               erreur_paragraphe=paragraphe_val)
    else:
        get_db().insert_article(titre, identifiant, auteur, date_publication, paragraphe)
        succes = "L'article %s à été ajouté avec succes" % titre
        #return render_template('admin.html', articles=articles, succes=succes)
        return redirect('/admin')


def validate_name(name, minimum, maximum, msg_min, msg_max):
    if len(name) <= minimum:
        return msg_min
    elif len(name) > maximum:
        return msg_max
    else:
        return ""


@app.errorhandler(404)
def not_found_page(e):
    return render_template('404.html'), 404


def validate_date(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
        date_reponse = ""
    except ValueError:
        date_reponse = "Le format de date est incorrecte, utiliser AAAA-MM-JJ"
    return date_reponse
