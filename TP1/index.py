# coding: utf8


from flask import Flask
from flask import render_template
from flask import g
from flask import request
from flask import redirect
from database import Database
from flask import make_response
from flask import request

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
    return render_template('accueil.html', publications=publications)


@app.route('/admin')
def admin_page():
    articles = get_db().get_all_article()
    return render_template('admin.html', articles=articles)


@app.route('/admin-modifier/<ident>')
def admin_edit_page(ident):
    article = get_db().get_article(ident)
    return render_template('admin-modifier.html', article=article)



# @app.route('/article/<identifiant>')
# def article_page(identifiant):
#     article = get_db().get_article(identifiant)
#     if article is None:
#         return render_template('404.html'), 404
#     else:
#         return render_template('article.html', article=article)


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

