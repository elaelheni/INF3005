# coding: utf8
#
# author: Jean-Michel Poirier
# code: POIJ26089200

import datetime
from flask import Flask
from flask import render_template
from flask import g
from flask import redirect
from flask import request
from flask import jsonify
from article import Article
import sys
import re

from flask import session
from flask import Response
from database import Database
import hashlib
import uuid
from functools import wraps
reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__, static_url_path="", static_folder="static")

MSG_ERR_TITRE_SHORT = "Le titre est obligatoire"
MSG_ERR_TITRE_LONG = "Le titre est trop long"
MSG_ERR_IDENT_SHORT = "L'identifiant est obligatoire"
MSG_ERR_IDENT_LONG = "L'identifiant est trop long"
MSG_ERR_IDENT_CAR_ILLEGAUX = "L'identifiant contient des caractères illegaux"
MSG_ERR_IDENT_NOT_UNIQUE = "L'idendifiant n'est pas unique"
MSG_ERR_AUTEUR_SHORT = "Le nom de l'auteur est obligatoire"
MSG_ERR_AUTEUR_LONG = "Le nom de l'auteur est trop long"
MSG_ERR_DATE_NOT_VALID = "Mauvais format de date! Utiliser AAAA-MM-JJ"
MSG_ERR_PARAGRAPHE_SHORT = "Le paragraphe est obligatoire"
MSG_ERR_PARAGRAPHE_LONG = "Le paragraphe est trop long"


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Article()
    return g._database


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.disconnect()


def authentification_required(f): # f est la fonction def logout
    @wraps(f)
    def decorated(*args, **kwargs):
        if not is_authenticated(session):
            return send_unauthorized()
        return f(*args, **kwargs)
    return decorated


@app.route('/')
def start_page():
    publications = get_db().get_cinq_last_publications()
    # username = None
    # if "id" in session:
    #     username = get_db().get_session(session["id"])
    # return render_template('accueil.html', username=username)
    return render_template('accueil.html', publications=publications)


@app.route('/admin')
@authentification_required
def admin_page():
    articles = get_db().get_all_articles()
    return render_template('admin.html', articles=articles)


@app.route('/article/<ident>')
def article_page(ident):
    article = get_db().get_article(ident)
    if article is None:
        return render_template('404.html'), 404
    else:
        return render_template('article.html', article=article)


@app.route('/recherche', methods=['POST'])
def recherche_page():
    rechercher = request.form['rechercher']
    like_recher = '%%%s%%' % rechercher
    articles = get_db().get_search_articles(like_recher)
    return render_template('recherche.html',
                           articles=articles,
                           rechercher=rechercher)


@app.route('/admin-modifier/<ident>')
@authentification_required
def admin_edit_page(ident):
    article = get_db().get_admin_article(ident)
    return render_template('admin-modifier.html', article=article)


@app.route('/admin-modifier-new', methods=['POST'])
@authentification_required
def admin_edit_form():
    identifier = request.form['identifier']
    titre = request.form['titre']
    paragraphe = request.form['paragraphe']
    get_db().uptade_article(identifier, titre, paragraphe)
    return redirect('/admin')


@app.route('/admin-form')
@authentification_required
def admin_add_form():
    return render_template('admin-form.html')


@app.route('/admin-form-new', methods=['POST'])
@authentification_required
def admin_post_form():
    titre = request.form['titre']
    identifiant = request.form['identifiant']
    auteur = request.form['auteur']
    date_pub = request.form['date_publication']
    paragraphe = request.form['paragraphe']

    titre_val = valide_form(titre, 0, 100,
                            MSG_ERR_TITRE_SHORT,
                            MSG_ERR_TITRE_LONG)
    ident_val = valide_ident(identifiant, 0, 50,
                             MSG_ERR_IDENT_SHORT,
                             MSG_ERR_IDENT_LONG,
                             MSG_ERR_IDENT_CAR_ILLEGAUX,
                             MSG_ERR_IDENT_NOT_UNIQUE)
    auteur_val = valide_form(auteur, 0, 100,
                             MSG_ERR_AUTEUR_SHORT,
                             MSG_ERR_AUTEUR_LONG)
    date_val = valide_date(date_pub)
    paragraphe_val = valide_form(paragraphe, 0, 500,
                                 MSG_ERR_PARAGRAPHE_SHORT,
                                 MSG_ERR_PARAGRAPHE_LONG)
    if titre_val != "" or ident_val != "" or auteur_val != "" or\
                    paragraphe_val != "" or date_val != "":
        return render_template('admin-form.html',
                               erreur_titre=titre_val,
                               erreur_ident=ident_val,
                               erreur_auteur=auteur_val,
                               erreur_date=date_val,
                               erreur_paragraphe=paragraphe_val,
                               titre=titre,
                               identifiant=identifiant,
                               auteur=auteur,
                               date=date_pub,
                               paragraphe=paragraphe), 400
    else:
        get_db().insert_article(titre, identifiant,
                                auteur, date_pub, paragraphe)
        return redirect('/admin')


# Apelle ajax
@app.route('/ident/<identifiant>')
def identifiant_replace(identifiant):
    nb_identifiant_pareil = 0
    identifiant_final = identifiant
    articles = get_db().get_all_articles()
    valid_ident_multiple = "%s%s" % (identifiant, "_[0-9][0-9]?[0-9]?$")
    for article in articles:
        if identifiant == article["identifiant"] or\
                re.match(valid_ident_multiple, article["identifiant"]):
            nb_identifiant_pareil += 1
            identifiant_final = "%s-%s" % (identifiant, nb_identifiant_pareil)
    return render_template('identifiant.html', identifiant=identifiant_final)


# API
@app.route('/api/articles/', methods=["GET", "POST"])
def liste_articles():
    if request.method == "GET":
        articles = get_db().get_all_articles()
        data = [{"titre": each["titre"], "auteur": each["auteur"],
                "URL": "%s%s" % ("http://127.0.0.1:5000/article/", each["identifiant"])} for each in articles]
        return jsonify(data)
    else:
        # Content-Type: application/json
        # {"titre":"titre", "identifiant":"identifiant", "auteur":"auteur", "date":"date", "paragraphe":"paragraphe"}
        data = request.get_json()
        get_db().insert_article(data["titre"], data["identifiant"],
                                data["auteur"], data["date"], data["paragraphe"])
        return "", 201 # 201 = La demande a été remplie et a entraîné la création d'une nouvelle ressource.



@app.route('/api/article/<ident>')
def un_article(ident):
    article = get_db().get_article(ident)
    if article is None:
        return render_template('404.html'), 404
    else:
        data = {"_id": article["id"], "titre": article["titre"],
                "auteur": article["auteur"],
                "date_publication": article["date_publication"],
                "paragraphe": article["paragraphe"]}
    return jsonify(data)


#Login
@app.route('/admin-login')
def admin_login():
    username = None
    if "id" in session:
        username = get_db().get_session(session["id"])
    return render_template('admin-login.html', username=username)


@app.route('/login', methods=["POST"])
def log_user():
    username = request.form["username"]
    password = request.form["password"]
    # Vérifier que les champs ne sont pas vides
    if username == "" or password == "":
        return redirect("/")

    user = get_db().get_user_login_info(username)
    if user is None:
        return redirect("/")

    salt = user[0]
    hashed_password = hashlib.sha512(password + salt).hexdigest()
    if hashed_password == user[1]:
        # Accès autorisé
        id_session = uuid.uuid4().hex  # genere identifiant aleatoire en hexadecimal
        get_db().save_session(id_session, username)
        session["id"] = id_session
        return redirect("/")
    else:
        return redirect("/")


@app.route('/logout')
@authentification_required
def logout():
    if "id" in session:
        id_session = session["id"]
        session.pop('id', None)
        get_db().delete_session(id_session)
    return redirect("/")


def is_authenticated(session):
    return "id" in session


def send_unauthorized():
    return redirect("/admin-login")
    # return Response('Could not verify your access level for that URL.\n'
    #                 'You have to login with proper credentials', 401,
    #                 {'WWW-Authenticate': 'Basic realm="Login Required"'})


app.secret_key = "(*&*&322387he738220)(*(*22347657"


@app.errorhandler(404)
def not_found_page(e):
    return render_template('404.html'), 404


def valide_form(name, minimum, maximum, msg_min, msg_max):
    if len(name) <= minimum:
        return msg_min
    elif len(name) > maximum:
        return msg_max
    else:
        return ""


def valide_ident(identifiant, minimum, maximum, msg_min, msg_max,
                 msg_car_illegaux, msg_not_unique):
    if not re.match("[A-Za-z0-9_-]*$", identifiant):
        return msg_car_illegaux
    if ident_not_unique(identifiant):
        return msg_not_unique
    else:
        return valide_form(identifiant, minimum, maximum, msg_min, msg_max)


def ident_not_unique(identifiant):
    articles = get_db().get_all_articles()
    ident_not_uni = False
    for article in articles:
        if identifiant == article["identifiant"]:
            ident_not_uni = True
    return ident_not_uni


def valide_date(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
        date_reponse = ""
    except ValueError:
        date_reponse = MSG_ERR_DATE_NOT_VALID
    return date_reponse
