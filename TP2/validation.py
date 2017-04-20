# coding: utf8
#
# author: Jean-Michel Poirier
# code: POIJ26089200

import datetime
import re

MSG_ERR_TITRE_SHORT = "Le titre est obligatoire"
MSG_ERR_TITRE_LONG = "Le titre est trop long"
MSG_ERR_IDENT_SHORT = "L'identifiant est obligatoire"
MSG_ERR_IDENT_LONG = "L'identifiant est trop long"
MSG_ERR_IDENT_CAR_ILLEGAUX = u"L'identifiant contient des caractères illegaux"
MSG_ERR_IDENT_NOT_UNIQUE = "L'idendifiant n'est pas unique"
MSG_ERR_AUTEUR_SHORT = "Le nom de l'auteur est obligatoire"
MSG_ERR_AUTEUR_LONG = "Le nom de l'auteur est trop long"
MSG_ERR_DATE_NOT_VALID = "Mauvais format de date! Utiliser AAAA-MM-JJ"
MSG_ERR_PARAGRAPHE_SHORT = "Le paragraphe est obligatoire"
MSG_ERR_PARAGRAPHE_LONG = "Le paragraphe est trop long"


def valide_article(titre, identifiant, auteur, date_pub, paragraphe, articles):
    titre_val = valide_form(titre, 0, 100,
                            MSG_ERR_TITRE_SHORT,
                            MSG_ERR_TITRE_LONG)
    ident_val = valide_ident(identifiant, 0, 50,
                             MSG_ERR_IDENT_SHORT,
                             MSG_ERR_IDENT_LONG,
                             MSG_ERR_IDENT_CAR_ILLEGAUX,
                             MSG_ERR_IDENT_NOT_UNIQUE, articles)
    auteur_val = valide_form(auteur, 0, 100,
                             MSG_ERR_AUTEUR_SHORT,
                             MSG_ERR_AUTEUR_LONG)
    date_val = valide_date(date_pub)
    paragraphe_val = valide_form(paragraphe, 0, 500,
                                 MSG_ERR_PARAGRAPHE_SHORT,
                                 MSG_ERR_PARAGRAPHE_LONG)
    dic = {'titre': titre_val, 'ident': ident_val, 'auteur': auteur_val, 'date': date_val, 'para': paragraphe_val}
    return dic


def valide_form(name, minimum, maximum, msg_min, msg_max):
    if len(name) <= minimum:
        return msg_min
    elif len(name) > maximum:
        return msg_max
    else:
        return ""


def valide_ident(identifiant, minimum, maximum, msg_min, msg_max,
                 msg_car_illegaux, msg_not_unique, articles):
    if not re.match("[A-Za-z0-9_-]*$", identifiant):
        return msg_car_illegaux
    if ident_not_unique(identifiant, articles):
        return msg_not_unique
    else:
        return valide_form(identifiant, minimum, maximum, msg_min, msg_max)


def ident_not_unique(identifiant, articles):
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
