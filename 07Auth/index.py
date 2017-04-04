# coding: utf8

from flask import Flask
from flask import render_template
from flask import g
from flask import request
from flask import redirect
from flask import session
from flask import Response
from database import Database
import hashlib
import uuid
from functools import wraps


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
    username = None
    if "id" in session:
        username = get_db().get_session(session["id"])
    return render_template('accueil.html', username=username)


@app.route('/confirmation')
def confirmation_page():
    return render_template('confirmation.html')


@app.route('/formulaire', methods=["GET", "POST"])
def formulaire_creation():
    if request.method == "GET":
        return render_template("formulaire.html")
    else:
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]
        # Vérifier que les champs ne sont pas vides
        if username == "" or password == "" or email == "":
            return render_template("formulaire.html", error="Tous les champs sont obligatoires.")
        # TODO Faire la validation du formulaire
        salt = uuid.uuid4().hex
        hashed_password = hashlib.sha512(password + salt).hexdigest()
        db = get_db()
        db.create_user(username, email, salt, hashed_password)
        return redirect("/confirmation")


# Fonction qui sert a rester connecter au site
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


def authentification_required(f): # f est la fonction def logout
    @wraps(f)
    def decorated(*args, **kwargs):
        if not is_authenticated(session):
            return send_unauthorized()
        return f(*args, **kwargs)
    return decorated


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
    return Response('Could not verify your access level for that URL.\n'
                    'You have to login with proper credentials', 401,
                    {'WWW-Authenticate': 'Basic realm="Login Required"'})


app.secret_key = "(*&*&322387he738220)(*(*22347657"