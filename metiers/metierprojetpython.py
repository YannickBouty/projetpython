from flask import request, jsonify
from werkzeug.utils import secure_filename
from datetime import datetime
from PIL import Image
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from metiers.entites.fichier import Fichier
import secrets

UPLOAD_DIRECTORY = './static/images/' # répertoire de stockage des fichiers
DATABASE = 'sqlite:///database/projetpython.db'

engine = create_engine(DATABASE)
Session = sessionmaker(bind=engine)

def retournerFichier(idfile):
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
    resultat = session.query(Fichier).filter(Fichier.identifiantMetier == idfile).one()
    return jsonify(resultat.serialise())

def enregistrerFichier(request):
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
    fichierEnvoye = request.files['monFichier']
    nomFichier = secure_filename(request.files['monFichier'].filename)
    extension = nomFichier.split(".")[-1].lower()
    mimeType = request.files['monFichier'].mimetype
    taille = request.headers.get('Content-Length')
    now = datetime.now()
    monGDH = now.strftime("%Y%m%d%H%M%S")
    #fichierEnvoye.save(UPLOAD_DIRECTORY + nouveauNom)
    try:
        with Image.open(fichierEnvoye) as monImage:
            monId = monGDH + secrets.token_hex(8)
            nouveauNom = monId + '.' + extension
            monImage.thumbnail((50,50))
            monImage.save(UPLOAD_DIRECTORY + nouveauNom)
            monFormat = monImage.format
            maLargeur, maHauteur = monImage.size
            monMode = monImage.mode
            #print(monFormat, maLargeur, maHauteur, monMode)
            #monImage.show()
        monFichier = Fichier(nomOrigine=nomFichier, extensionOrigine=extension, \
                mimeTypeOrigine=mimeType, tailleOrigine=taille, \
                identifiantMetier=monId, nouveauNom=nouveauNom, \
                nouveauFormat=monFormat, nouvelleLargeur=maLargeur,\
                nouvelleHauteur=maHauteur, nouveauMode=monMode)
        session.add(monFichier)
        session.commit()
        return monId
    except OSError:
        return 'Une erreur est survenue lors du traitement du fichier.'
