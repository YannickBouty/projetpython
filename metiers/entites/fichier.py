from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Fichier(Base):
    __tablename__ = 'fichier'
    id = Column(Integer, primary_key=True)
    nomOrigine = Column(String)
    extensionOrigine = Column(String)
    mimeTypeOrigine = Column(String)
    tailleOrigine = Column(String)
    identifiantMetier = Column(String)
    nouveauNom = Column(String)
    nouveauFormat = Column(String)
    nouvelleLargeur = Column(String)
    nouvelleHauteur = Column(String)
    nouveauMode = Column(String)

    def serialise(self):
        monUrl = 'http://127.0.0.1:5000/static/images/' + self.nouveauNom
        result = {
                'Nom origine': self.nomOrigine,
                'Extension origine': self.extensionOrigine,
                'MimeType origine': self.mimeTypeOrigine,
                'Taille origine en octets': self.tailleOrigine,
                'Identifiant métier': self.identifiantMetier,
                'Nouveau nom': self.nouveauNom,
                'Nouveau format': self.nouveauFormat,
                'Nouvelle largeur en pixels': self.nouvelleLargeur,
                'Nouvelle hauteur en pixels': self.nouvelleHauteur,
                'Nouveau mode': self.nouveauMode,
                'url': monUrl
        }
        return result
