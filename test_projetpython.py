import unittest
from requests.auth import _basic_auth_str
from projetpython import app


class TestProjetPython(unittest.TestCase):

    def test_getFileById_userOk_idFileOk(self):
        with app.test_client() as client:
            username = 'benoitlarroque'
            password = 'mssio'
            maReponse = client.get('/getfilebyid/2020110421321409bbca3a8bc73036', \
                    headers={'Authorization': _basic_auth_str(username, password)})
            maReponseJson = maReponse.get_json()
            monIdentifiantFichier = maReponseJson['Identifiant métier']
            self.assertEqual(monIdentifiantFichier, '2020110421321409bbca3a8bc73036')

    def test_getFileById_userOk_idFileKo(self):
        with app.test_client() as client:
            username = 'benoitlarroque'
            password = 'mssio'
            maReponse = client.get('/getfilebyid/20201djvbmzkdivbmz23036', \
                    headers={'Authorization': _basic_auth_str(username, password)})
            self.assertIn(b'Identifiant incorrect !\n', maReponse.data)
    
    def test_getFileById_userOk_idFileVide(self):
        with app.test_client() as client:
            username = 'benoitlarroque'
            password = 'mssio'
            maReponse = client.get('/getfilebyid/', \
                    headers={'Authorization': _basic_auth_str(username, password)})
            self.assertEqual(maReponse.status_code, 404)
    
    def test_getFileById_userKo_idFileOk(self):
        with app.test_client() as client:
            username = 'utilisateur'
            password = 'mdp'
            maReponse = client.get('/getfilebyid/2020110421321409bbca3a8bc73036', \
                    headers={'Authorization': _basic_auth_str(username, password)})
            self.assertEqual(maReponse.status_code, 401)
    
    def test_getFileById_userOk_idFileOkInconnu(self):
        with app.test_client() as client:
            username = 'benoitlarroque'
            password = 'mssio'
            maReponse = client.get('/getfilebyid/2020110421321409bbca3a8bc456ca', \
                    headers={'Authorization': _basic_auth_str(username, password)})
            self.assertEqual(maReponse.status_code, 500)
    
    def test_mauvaiseUrl(self):
        with app.test_client() as client:
            username = 'benoitlarroque'
            password = 'mssio'
            maReponse = client.get('/', \
                    headers={'Authorization': _basic_auth_str(username, password)})
            self.assertEqual(maReponse.status_code, 404)
