DROP TABLE IF EXISTS fichier;

CREATE TABLE IF NOT EXISTS fichier(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nomOrigine TEXT,
	extensionOrigine TEXT,
	mimeTypeOrigine TEXT,
	tailleOrigine TEXT,
	identifiantMetier TEXT,
	nouveauNom TEXT,
	nouveauFormat TEXT,
	nouvelleLargeur TEXT,
	nouvelleHauteur TEXT,
	nouveauMode TEXT
);
