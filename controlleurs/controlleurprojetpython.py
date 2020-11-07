"""
Script de contrôle du projet.
"""

from werkzeug.utils import secure_filename
import metiers.metierprojetpython

#fichiers authorisés
ALLOWED_EXTENSIONS = ['gif','jpeg','jpg','png']

def aiguiller():
    """
    Renvoie tous les identifiants métiers des images.
    Returns
    -------
    Tableau d'identifiants métier : [string]
    """
    return metiers.metierprojetpython.retourner_all_id_metier()

def controler_format(request):
    """
    Contrôle si l'extension du fichier est autorisée et en fonction oriente le traitement.
    Parameters
    ----------
    request : flask.request
    Returns
    -------
    Retourne l'identifiant de l'image enregistrée.

    """
    fichier_envoye = request.files['monFichier']
    nom_fichier = secure_filename(fichier_envoye.filename)
    #fichier bien envoyé?
    if fichier_envoye:
        #extension valide ?
        if '.' in nom_fichier and nom_fichier.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS:
            return metiers.metierprojetpython.enregistrer_fichier(request)
        else:
            return 'Accès autorisé mais le fichier ne porte pas une extension autorisée !\n'
    else:
        return 'Accès autorisé mais vous avez oublié le fichier en paramètre !\n'

def controler_identifiant(idfile):
    """
    Contrôle si la variable passée en paramètre n'est pas vide et si sa taille est de 22 caractères.
    Parameters
    ----------
    Identifiant : string
    Returns
    -------
    Métadonnées : json
    """
    if idfile not in (None, ''):
        if len(idfile) == 30:
            return metiers.metierprojetpython.retourner_fichier(idfile)
        else :
            return 'Identifiant incorrect !\n'
    else:
        return 'Identifiant incorrect !\n'
