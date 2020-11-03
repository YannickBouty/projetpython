from flask import request
from werkzeug.utils import secure_filename
import metiers.metierprojetpython

ALLOWED_EXTENSIONS = ['gif','jpeg','jpg','png'] # fichiers authorisés
UPLOAD_DIRECTORY = './uploadfiles/' # répertoire de stockage des fichiers

def controlerFormat(request):
    """
    Contrôle si l'extension du fichier est autorisée et en fonction oriente le traitement.
    
    Parameters
    ----------
    request : flask.request

    Returns
    -------
    Retourne l'identifiant de l'image enregistrée.

    """
    fichierEnvoye = request.files['monFichier']
    nomFichier = secure_filename(fichierEnvoye.filename)
    if fichierEnvoye: # je vérifie qu'un fichier a bien été envoyé
        if ('.' in nomFichier and nomFichier.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS): #extension valide ?
            return metiers.metierprojetpython.enregistrerFichier(request)
        else:
            return 'Accès autorisé mais le fichier ne porte pas une extension autorisée !\n'
    else:
        return 'Accès autorisé mais vous avez oublié le fichier en paramètre !\n'

def controlerIdentifiant(idfile):
    """
    Contrôle si la variable passée en paramètre n'est pas vide et si sa taille est de 22 caractères.

    Parameters
    ----------
    Identifiant : string

    Returns
    -------
    Métadonnées : json
    """
    if (idfile not in (None, '')):
        if (len(idfile) == 30):
            return metiers.metierprojetpython.retournerFichier(idfile)
        else :
            return 'Identifiant incorrect !\n'
    else:
        return 'Identifiant incorrect !\n'
