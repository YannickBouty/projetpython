"""
Script principal fournisseur des services.
"""

import hashlib
from flask import Flask, request, abort
from werkzeug.exceptions import RequestEntityTooLarge
import controlleurs.controlleurprojetpython

app = Flask(__name__)
#limite la taille des fichiers à uploader à 1Mo
app.config["MAX_CONTENT_LENGTH"]=1*1024*1024
#pour les caractères accentués dans le JSON de retour
app.config['JSON_AS_ASCII'] = False

#nom de l'utilisateur hashé
NOM_UTILISATEUR = '05cfcf0c489eb08ea4af6b2ad6b215770d01984f33fd262d314a034b4d7141cb'
#mot de passe de l'utilisateur hashé
MOT_DE_PASSE = '8f21ee6dc94c3a780ac0ff891c36b343ae0db7ee5cbf4fb4ac496ade5c4c94f4'

def authorisation_acces():
    """
    Autorise l'accès.
    Parameters
    ----------
    request : flask.request
    Returns
    -------
    boolean
    """
    #récupération de l'utilisateur passé en paramètre du curl
    user = request.authorization
    #hashage du nom et du mot de passe
    nom_utilisateur_hash = hashlib.sha256(user.username.encode()).hexdigest()
    mot_de_passe_hash = hashlib.sha256(user.password.encode()).hexdigest()
    #authorisation ok : retourne True
    return bool(nom_utilisateur_hash==NOM_UTILISATEUR and mot_de_passe_hash==MOT_DE_PASSE)

@app.route('/getall')
def get_all():
    """
    Ce service web renvoie tous les identifiants métiers des images.
    Returns
    -------
    Tableau d'identifiants métier : [string]
    """
    if authorisation_acces():
        # Auhtorisation d'accès
        return controlleurs.controlleurprojetpython.aiguiller()
    else:
        abort(401)

@app.route('/getfilebyid/<idfile>')
def get_file_by_id(idfile):
    """
    Ce service web permet de récupérer les métadonnées d'une image déposée par son id.
    Parameters
    ----------
    idfile : string
    Returns
    -------
    Métadonnées : json
    """
    if authorisation_acces():
        # Authorisation d'accès
        return controlleurs.controlleurprojetpython.controler_identifiant(idfile)
    else:
        abort(401)

@app.route('/uploadfile', methods=['POST'])
def upload_file():
    """
    Ce service web permet le dépôt d'images au format ['gif','jpeg','jpg','png'] et de taille < 1Mo
    et retourne l'identifiant de l'image enregistrée.
    Returns
    -------
    identifiant : string
    """
    if authorisation_acces():
        # Authorisation d'accès
        return controlleurs.controlleurprojetpython.controler_format(request)
    else:
        abort(401)

@app.errorhandler(401)
@app.errorhandler(404)
@app.errorhandler(413)
@app.errorhandler(500)
@app.errorhandler(RequestEntityTooLarge)
def page_erreur(error):
    """
    Cette fonction retourne le message d'erreur approprié.
    Parameters
    ----------
    error : int
    Returns
    -------
    Une phrase expliquant l'erreur avec le numéro de celle-ci : string
    """
    return 'Vous avez rencontré une erreur {}.\n'.format(error.code), error.code
