# coding: utf8

from flask import Flask
from flask import render_template
from flask import redirect
from flask import request

app = Flask(__name__)


@app.route('/')
def formulaire():
    return render_template('formulaire.html')

@app.route('/envoyer', methods=['POST'])
def donnes_formulaire():
    print request.form['name']
    print request.form['fname']
    print request.form['birthday']
    print request.form['birthmonth']
    print request.form['birthyear']
    print request.form['email']
    print request.form['username']
    print request.form['password']
    print request.form['salary']
    print request.form['publicity']
    print request.form['rating']
    # Excellent endroit pour valider les données et les sauvegarder dans une
    # base de données.
    # Prévoir une route pour afficher les erreurs.
    return redirect('/merci')

@app.route('/merci')
def merci():
    return render_template('merci.html')