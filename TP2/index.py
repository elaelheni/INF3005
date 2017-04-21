# coding: utf8
#
# author: Jean-Michel Poirier
# code: POIJ26089200

from validation import *
from gmail import *
from flask import Flask
from flask import render_template
from flask import g
from flask import redirect
from flask import request
from flask import jsonify
from users import Users
import re
from flask import session
from datetime import datetime
from datetime import timedelta
import hashlib
import uuid
from functools import wraps

app = Flask(__name__, static_url_path="", static_folder="static")


MSG_USER_ADDED = u"Votre compte à été créer avec succès"
MSG_ERR_USERNAME_SAME = u"Ce nom d'utilisateur existe déjà"
MSG_ERR_LOGIN = "Votre nom d'utilisateur et/ou votre mot de passe " \
                "est/sont incorrect"
MSG_EMAIL_NOT_FOUND = "Mauvais courriel"
MSG_EMAIL_WRONG_FORMAT = u"Le courriel entré à un mauvais format"
MSG_EMAIL_SENT = u"Un courriel vous à été envoyer"
MSG_EMAIL_SENT_TO_USER = u"Un courriel à été envoyer"
MSG_EMAIL_DEJA_EXISTE = u"Un utilisateur possède déjà ce courriel"
MSG_PASS_MODIF = u"Votre mot de passe à été modifier avec succès"
MSG_ERR_PASSWORD_SHORT = "Le mot de passe est trop court"
MSG_ERR_PASSWORD_LONG = "Le mot de passe est trop long"
MSG_ERR_PASSWORD_DIFF = u"Les mots de passe sont différents"


# Varabile de la date d'expiration d'une demande de
# réinitialisation de mot de passe ou d'une invitation.
date_passe = datetime.strptime("2000-08-14 11:42:17.001337",
                               "%Y-%m-%d %H:%M:%S.%f")
date_futur = datetime.now() + timedelta(minutes=15)
date_present = datetime.now()


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Users()
    return g._database


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.disconnect()


def authentification_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not is_authenticated(session):
            return send_unauthorized()
        return f(*args, **kwargs)
    return decorated


@app.route('/')
def start_page():
    publications = get_db().get_cinq_last_publications()
    username = username_session()
    return render_template('accueil.html', publications=publications,
                           username=username)


@app.route('/invite/<token>')
def invite_page(token):
    username = username_session()
    if username is None:
        try:
            email = get_db().get_email_new_user(token)
            date_exp_string = str(email["expiration"])
            date_exp = datetime.strptime(date_exp_string,
                                         "%Y-%m-%d %H:%M:%S.%f")
        except Exception:
            return render_template('404.html'), 404
        if email["email"] is None or date_exp < date_present:
            return render_template('404.html'), 404
        else:
            return render_template('invite.html',
                                   email=email["email"])
    else:
        return redirect('/admin-login')


@app.route('/invite-add-user', methods=['POST'])
def invite():
    username = request.form['username']
    email = request.form['courriel-form']
    password = request.form['password']
    password_repeat = request.form['password-repeat']
    users = get_db().get_users()
    for user in users:
        if username == user["utilisateur"]:
            return render_template('invite.html', user=username,
                                   email=email,
                                   erreur_user_same=MSG_ERR_USERNAME_SAME), 400
    dic = valide_invi(username, password, password_repeat)
    if dic['user'] != "" or dic['pass'] != "":
        return render_template('invite.html', user=username, email=email,
                               erreur_user=dic['user'],
                               erreur_pass=dic['pass']), 400
    else:
        get_db().uptade_user(email, date_passe)
        salt = uuid.uuid4().hex
        hashed_password = hashlib.sha512(password + salt).hexdigest()
        get_db().insert_user(username, email, salt, hashed_password)
        return render_template('compte-creer.html',
                               user_added=MSG_USER_ADDED), 201


@app.route('/reset-password')
def reset_password_page():
    username = username_session()
    if username is None:
        return render_template('reset-password.html')
    else:
        return redirect('/admin-login')


@app.route('/reset', methods=['POST'])
def reset_password():
    courriel = request.form['courriel']
    emails = get_db().get_emails()
    for email in emails:
        if courriel == email["email"]:
            email_token = u"%s%s" % (uuid.uuid4(), "")
            url = u"%s%s%s" % (request.url_root, "nouveau-password/",
                               email_token)
            get_db().insert_reset_password(courriel, email_token, date_futur)
            envoyer_email(courriel, url, 1)
            return render_template('reset-password.html',
                                   email_sent=MSG_EMAIL_SENT)
    return render_template('reset-password.html',
                           erreur_no_email=MSG_EMAIL_NOT_FOUND,
                           courriel=courriel)


@app.route('/nouveau-password/<token>')
def nouveau_password_page(token):
    username = username_session()
    if username is None:
        try:
            email = get_db().get_email(token)
            date_exp_string = str(email["expiration"])
            date_exp = datetime.strptime(date_exp_string,
                                         "%Y-%m-%d %H:%M:%S.%f")
        except Exception:
            return render_template('404.html'), 404
        if email["email"] is None or date_exp < date_present:
            return render_template('404.html'), 404
        else:
            return render_template('nouveau-password.html',
                                   email=email["email"])
    else:
        return redirect('/admin-login')


@app.route('/nouveau-password-update', methods=['POST'])
def nouveau_password():
    email = request.form['courriel-form']
    password = request.form['password']
    password_repeat = request.form['password-repeat']
    if password != password_repeat:
        return render_template('nouveau-password.html', email=email,
                               erreur_pass_same=MSG_ERR_PASSWORD_DIFF), 400
    elif len(password) <= 5:
        return render_template('nouveau-password.html', email=email,
                               erreur_pass_short=MSG_ERR_PASSWORD_SHORT), 400
    elif len(password) >= 30:
        return render_template('nouveau-password.html', email=email,
                               erreur_pass_long=MSG_ERR_PASSWORD_LONG), 400
    else:
        salt = uuid.uuid4().hex
        hashed_password = hashlib.sha512(password + salt).hexdigest()
        get_db().uptade_password(email, salt, hashed_password)
        return render_template('nouveau-password.html', email=email,
                               pass_modif=MSG_PASS_MODIF), 201


@app.route('/admin')
@authentification_required
def admin_page():
    articles = get_db().get_all_articles()
    username = username_session()
    return render_template('admin.html', articles=articles, username=username)


@app.route('/article/<ident>')
def article_page(ident):
    article = get_db().get_article(ident)
    username = username_session()
    if article is None:
        return render_template('404.html', username=username), 404
    else:
        return render_template('article.html', article=article,
                               username=username)


@app.route('/recherche', methods=['POST'])
def recherche_page():
    rechercher = request.form['rechercher']
    like_recher = '%%%s%%' % rechercher
    articles = get_db().get_search_articles(like_recher)
    username = username_session()
    return render_template('recherche.html',
                           articles=articles,
                           rechercher=rechercher, username=username)


@app.route('/admin-modifier/<ident>')
@authentification_required
def admin_edit_page(ident):
    article = get_db().get_admin_article(ident)
    username = username_session()
    return render_template('admin-modifier.html', article=article,
                           username=username)


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
    username = username_session()
    return render_template('admin-form.html', username=username)


@app.route('/admin-form-new', methods=['POST'])
@authentification_required
def admin_post_form():
    titre = request.form['titre']
    identifiant = request.form['identifiant']
    auteur = request.form['auteur']
    date_pub = request.form['date_publication']
    paragraphe = request.form['paragraphe']
    articles = get_db().get_all_articles()
    dic = valide_article(titre, identifiant, auteur,
                         date_pub, paragraphe, articles)
    username = username_session()
    if dic['titre'] != "" or dic['ident'] != "" or dic['auteur'] != ""\
            or dic['para'] != "" or dic['date'] != "":
        return render_template('admin-form.html',
                               erreur_titre=dic['titre'],
                               erreur_ident=dic['ident'],
                               erreur_auteur=dic['auteur'],
                               erreur_date=dic['date'],
                               erreur_paragraphe=dic['para'],
                               titre=titre,
                               identifiant=identifiant,
                               auteur=auteur,
                               date=date_pub,
                               paragraphe=paragraphe,
                               username=username), 400
    else:
        get_db().insert_article(titre, identifiant,
                                auteur, date_pub, paragraphe)
        return render_template('admin.html', articles=articles,
                               username=username), 201


@app.route('/admin-add-user')
@authentification_required
def admin_add_user_page():
    username = username_session()
    return render_template('admin-add-user.html', username=username)


@app.route('/admin-add-user-new', methods=['POST'])
@authentification_required
def admin_add_user():
    courriel = request.form['courriel']
    if courriel is None or courriel == "" or "@" not in courriel:
        username = username_session()
        return render_template('admin-add-user.html',
                               erreur_email=MSG_EMAIL_WRONG_FORMAT,
                               username=username)
    emails = get_db().get_emails()
    for email in emails:
        if courriel == email["email"]:
            username = username_session()
            return render_template('admin-add-user.html',
                                   erreur_email=MSG_EMAIL_DEJA_EXISTE,
                                   username=username)
    email_token = u"%s%s" % (uuid.uuid4(), "")
    url = u"%s%s%s" % (request.url_root, "invite/", email_token)
    get_db().insert_new_user(courriel, email_token, date_futur)
    envoyer_email(courriel, url, 2)
    username = username_session()
    return render_template('admin-add-user.html',
                           email_sent=MSG_EMAIL_SENT_TO_USER,
                           username=username)


# Apelle ajax
@app.route('/ident/<identifiant>')
def identifiant_replace(identifiant):
    nb_identifiant_pareil = 0
    identifiant_final = identifiant
    articles = get_db().get_all_articles()
    valid_ident_multiple = "%s%s" % (identifiant, "-[0-9][0-9]?[0-9]?$")
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
                 "URL": "%s%s%s" % (request.url_root, "article/",
                                    each["identifiant"])} for each in articles]
        return jsonify(data)
    else:
        data = request.get_json()
        articles = get_db().get_all_articles()
        dic = valide_article(data["titre"], data["identifiant"],
                             data["auteur"], data["date"],
                             data["paragraphe"], articles)
        if dic['titre'] != "" or dic['ident'] != "" or dic['auteur'] != "" \
                or dic['para'] != "" or dic['date'] != "":
            return "Non valide", 400
        else:
            get_db().insert_article(data["titre"], data["identifiant"],
                                    data["auteur"], data["date"],
                                    data["paragraphe"])
        return "", 201


@app.route('/api/article/<ident>', methods=['GET'])
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


@app.route('/admin-login')
def admin_login():
    username = username_session()
    return render_template('admin-login.html', username=username)


@app.route('/login', methods=["POST"])
def log_user():
    username = request.form["username"]
    password = request.form["password"]
    # Vérifier que les champs ne sont pas vides
    if username == "" or password == "":
        return redirect("/admin-login")

    user = get_db().get_user_login_info(username)
    if user is None:
        return render_template("admin-login.html", username_log=username,
                               erreur_login=MSG_ERR_LOGIN)
    salt = user[0]
    hashed_password = hashlib.sha512(password + salt).hexdigest()
    if hashed_password == user[1]:
        # Accès autorisé
        id_session = uuid.uuid4().hex
        get_db().save_session(id_session, username)
        session["id"] = id_session
        return redirect("/admin")
    else:
        return render_template("admin-login.html", username_log=username,
                               erreur_login=MSG_ERR_LOGIN)


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


def username_session():
    username = None
    if "id" in session:
        username = get_db().get_session(session["id"])
    return username


def send_unauthorized():
    return render_template('admin-login.html'), 401


app.secret_key = "(*&*&322387he738220)(*(*22347657"


@app.errorhandler(404)
def not_found_page(e):
    username = username_session()
    return render_template('404.html', username=username), 404
