"""
Script métier du projet.
"""

from datetime import datetime
import secrets
from flask import jsonify
from werkzeug.utils import secure_filename
from PIL import Image
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm.exc import NoResultFound
from metiers.entites.fichier import Fichier

UPLOAD_DIRECTORY = './static/images/' # répertoire de stockage des fichiers
DATABASE = 'sqlite:///database/projetpython.db'

engine = create_engine(DATABASE)
Session = sessionmaker(bind=engine)

def retourner_fichier(idfile):
    """
    Retourne les métadonnées enregistrées en base de données d'un fichier uploadé.
    Parameters
    ----------
    Identifiant : string
    Return
    ------
    Métadonnées : json
    """
    session = Session()
    try:
        resultat = session.query(Fichier).filter(Fichier.identifiantMetier == idfile).one()
        return jsonify(resultat.serialise())
    except NoResultFound:
        return 'Aucune image ne correspond !\n'

def enregistrer_fichier(request):
    """
    Enregistre l'image en vignette, enregistre les métadonnées en base de données
    et retourne l'identifiant de l'image enregistrée.
    Parameters
    ----------
    request : flask.request
    Returns
    -------
    Retourne l'identifiant de l'image enregistrée.
    """
    session = Session()
    fichier_envoye = request.files['monFichier']
    nom_fichier = secure_filename(request.files['monFichier'].filename)
    extension = nom_fichier.split(".")[-1].lower()
    mime_type = request.files['monFichier'].mimetype
    taille = request.headers.get('Content-Length')
    #now = datetime.now()
    #mon_gdh = now.strftime("%Y%m%d%H%M%S")
    try:
        with Image.open(fichier_envoye) as mon_image:
            mon_id = datetime.now().strftime("%Y%m%d%H%M%S") + secrets.token_hex(8)
            nouveau_nom = mon_id + '.' + extension
            mon_image.thumbnail((50,50))
            mon_image.save(UPLOAD_DIRECTORY + nouveau_nom)
            mon_format = mon_image.format
            ma_largeur, ma_hauteur = mon_image.size
            mon_mode = mon_image.mode
            #monImage.show()
        mon_fichier = Fichier(nomOrigine=nom_fichier, extensionOrigine=extension, \
                mimeTypeOrigine=mime_type, tailleOrigine=taille, \
                identifiantMetier=mon_id, nouveauNom=nouveau_nom, \
                nouveauFormat=mon_format, nouvelleLargeur=ma_largeur,\
                nouvelleHauteur=ma_hauteur, nouveauMode=mon_mode)
        session.add(mon_fichier)
        session.commit()
        return mon_id
    except OSError:
        return 'Une erreur est survenue lors du traitement du fichier.'
