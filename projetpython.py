from flask import Flask, request, abort
from werkzeug.exceptions import RequestEntityTooLarge
import hashlib
import controlleurs.controlleurprojetpython

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"]=1*1024*1024 #limite la taille des fichiers à 1Mo
app.config['JSON_AS_ASCII'] = False #Pour les caractères accentués dans le JSON

NOM_UTILISATEUR = '05cfcf0c489eb08ea4af6b2ad6b215770d01984f33fd262d314a034b4d7141cb' # nom de l'utilisateur hashé
MOT_DE_PASSE = '8f21ee6dc94c3a780ac0ff891c36b343ae0db7ee5cbf4fb4ac496ade5c4c94f4' # mot de passe de l'utilisateur hashé

def authorisationAcces(request):
    """
    Autorise l'accès.

    Parameters
    ----------
    request : flask.request

    Returns
    -------
    boolean
    """
    user = request.authorization # récupération de l'utilisateur passé en paramètre du curl
    nomUtilisateurHash = hashlib.sha256(user.username.encode()).hexdigest() # hashage du nom
    motDePasseHash = hashlib.sha256(user.password.encode()).hexdigest() # hashage du mot de passe
    if (nomUtilisateurHash==NOM_UTILISATEUR and motDePasseHash==MOT_DE_PASSE):
        # Authorisation d'accès
        return True
    else:
        return False

@app.route('/getfilebyid/<idfile>')
def getFileById(idfile):
    """
    Ce service web permet de récupérer les métadonnées d'une image déposée par son id.
    
    Parameters
    ----------
    idfile : string

    Returns
    -------
    Métadonnées : json
    """
    if (authorisationAcces(request)):
        # Authorisation d'accès
        return controlleurs.controlleurprojetpython.controlerIdentifiant(idfile)
    else:
        abort(401)

@app.route('/uploadFile', methods=['POST'])
def uploadFile():
    """
    Ce service web permet le dépôt d'images au format ['gif','jpeg','jpg','png'] et de taille < 1Mo
    et retourne l'identifiant de l'image enregistrée.

    Returns
    -------
    identifiant : string
    """
    if (authorisationAcces(request)):
        # Authorisation d'accès
        return controlleurs.controlleurprojetpython.controlerFormat(request)
    else:
        abort(401)

@app.errorhandler(401)
@app.errorhandler(404)
@app.errorhandler(413)
@app.errorhandler(500)
@app.errorhandler(RequestEntityTooLarge)
def pageErreur(error):
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
