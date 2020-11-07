Centrale Supelec-MS SIO 2020-YANNICK BOUTY

------------------------------------------
	RECUPERATION PROJET
------------------------------------------
1/Installer git
Exemple sous FreeBSD : sudo pkg install git
2/Dans une console, placer vous dans votre répertoire de travail et récupérer le projet avec la commande :
git clone https://github.com/YannickBouty/projetpython.git

------------------------------------------
	INSTALLATION
------------------------------------------
1/Installer python
Exemple sous FreeBSD : sudo pkg install python
2/Installer pip
Exemple sous FreeBSD : sudo pkg install py37-pip
3/Installer les packages requis
Exemple : pip install -r requirements.txt

------------------------------------------
	LANCEMENT DU SERVEUR
------------------------------------------
Dans une console, lancer le serveur avec la commande :
./lancement-serveur-projetpython.sh

Si le fichier ne s'exécute pas, il faut lui donner les droits d'exécution :
chmod 744 lancement-serveur-projetpython.sh

------------------------------------------
	TESTER LES SERVICES
------------------------------------------
Dans une console :
1/Test du service d'upload d'images :
Les images autorisées sont les png, jpeg, jpg et gif de taille max d'1Mo.
Une authentification est nécessaire avec : username = benoitlarroque et password = mssio

Exemple : curl -X POST -u "benoitlarroque:mssio" http://127.0.0.1:5000/uploadfile -F 'monFichier=@./testfiles/python.png'

NOTER LA CHAINE DE CARACTERES RETOURNEE ! Il s'agit de l'identifiant métier pour afficher les informations de l'image uploadée.

2/Test du service de récupération des métadonnées et de l'url d'accès à la vignette :
Une authentification est nécessaire avec : username = benoitlarroque et password = mssio

Exemple : curl -u "benoitlarroque:mssio" "http://127.0.0.1:5000/getfilebyid/IdentifiantMetier"

Vous pouvez cliquer sur le lien proposé pour afficher la vignette dans votre navigateur.

3/Test du service de récupération de tous les identifiants métier des images connues :
Une authentification est nécessaire avec : username = benoitlarroque et password = mssio

Exemple : curl -u "benoitlarroque:mssio" http://127.0.0.1:5000/getall

NOTER LES CHAINES DE CARACTERES RETOURNEES ! Il s'agit des identifiants métier pour afficher les informations des images uploadées.

4/Dans le fichier "automatisation-tests-fonctionnels-projetpython.sh", vous trouverez des exemples de tests fonctionnels.
Vous pouvez l'exécuter avec la commande :
./automatisation-tests-fonctionnels-projetpython.sh

Si le fichier ne s'exécute pas, il faut lui donner les droits d'exécution :
chmod 744 automatisation-tests-fonctionnels-projetpython.sh

------------------------------------------
	TESTS UNITAIRES
------------------------------------------
Dans une console à la racine du projet, exécuter la commande :
pytest -sv

------------------------------------------
	CONNAISSANCES MISE EN OEUVRE
------------------------------------------
Langage script et cURL
Langage Python (flask, try/except, SQLAlchemy, Pillow, class, ORM, hashage, etc.)
Langage SQL
Installation de packages
Architecture MVC (sans les templates ...)
Mise en oeuvre du base de données
Tests unitaires
Qualité de code avec pylint (respect de la PEP)
Versionning des sources avec GIT et GITHUB

------------------------------------------
	AMELIORATIONS
------------------------------------------
Je n'ai pas mis en oeuvre la mise en file des messages car je n'ai pas compris ce chapitre en cours.


