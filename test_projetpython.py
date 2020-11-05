import unittest
import io
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
            self.assertIn(b'Aucune image ne correspond !\n', maReponse.data)
    
    def test_mauvaiseUrl(self):
        with app.test_client() as client:
            username = 'benoitlarroque'
            password = 'mssio'
            maReponse = client.get('/', \
                    headers={'Authorization': _basic_auth_str(username, password)})
            self.assertEqual(maReponse.status_code, 404)

    def test_uploadFile_userOk_fileOk(self):
        with app.test_client() as client:
            username = 'benoitlarroque'
            password = 'mssio'
            with open('./testfiles/python.png','rb') as monImage:
                monImageIO = io.BytesIO(monImage.read())
            maData = {'monFichier': (monImageIO, 'python.png')}
            maReponse = client.post('/uploadfile', headers={'Authorization': _basic_auth_str(username, password)}, \
                    data=maData, content_type='multipart/form-data')
            self.assertEqual(len(maReponse.data.decode('UTF-8')), 30)
    
    def test_uploadFile_userKo_fileOk(self):
        with app.test_client() as client:
            username = 'utilisateur'
            password = 'mdp'
            with open('./testfiles/python.png','rb') as monImage:
                monImageIO = io.BytesIO(monImage.read())
            maData = {'monFichier': (monImageIO, 'python.png')}
            maReponse = client.post('/uploadfile', headers={'Authorization': _basic_auth_str(username, password)}, \
                    data=maData, content_type='multipart/form-data')
            self.assertEqual(maReponse.status_code, 401)
    
    def test_uploadFile_userOk_fileBig(self):
        with app.test_client() as client:
            username = 'benoitlarroque'
            password = 'mssio'
            with open('./testfiles/bigimg.png','rb') as monImage:
                monImageIO = io.BytesIO(monImage.read())
            maData = {'monFichier': (monImageIO, 'bigimg.png')}
            maReponse = client.post('/uploadfile', headers={'Authorization': _basic_auth_str(username, password)}, \
                    data=maData, content_type='multipart/form-data')
            self.assertEqual(maReponse.status_code, 413)
    
    def test_uploadFile_userOk_fileEntensionKo(self):
        with app.test_client() as client:
            username = 'benoitlarroque'
            password = 'mssio'
            with open('./testfiles/data.sql','rb') as monImage:
                monImageIO = io.BytesIO(monImage.read())
            maData = {'monFichier': (monImageIO, 'data.sql')}
            maReponse = client.post('/uploadfile', headers={'Authorization': _basic_auth_str(username, password)}, \
                    data=maData, content_type='multipart/form-data')
            self.assertIn(b'Acc\xc3\xa8s autoris\xc3\xa9 mais le fichier ne porte pas une extension autoris\xc3\xa9e !\n', \
                    maReponse.data)
