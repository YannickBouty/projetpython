#!/bin/bash
#Début tests
echo '------------------------------------------------------------------------'
echo 'DEBUT TESTS'
echo '------------------------------------------------------------------------'
echo 'TESTS UPLOAD OK'
echo '------------------------------------------------------------------------'
#Test : user ok, fichier existant et extension ok en minuscule ou majuscule
monTestUn=$(curl -X POST -u "benoitlarroque:mssio" http://127.0.0.1:5000/uploadFile -F 'monFichier=@./testfiles/angular.jpeg' 2>/dev/null)
echo "$monTestUn"
monTestDeux=$(curl -X POST -u "benoitlarroque:mssio" http://127.0.0.1:5000/uploadFile -F 'monFichier=@./testfiles/java.jpg' 2>/dev/null)
echo "$monTestDeux"
monTestTrois=$(curl -X POST -u "benoitlarroque:mssio" http://127.0.0.1:5000/uploadFile -F 'monFichier=@./testfiles/python.png' 2>/dev/null)
echo "$monTestTrois"
monTestQuatre=$(curl -X POST -u "benoitlarroque:mssio" http://127.0.0.1:5000/uploadFile -F 'monFichier=@./testfiles/react.PNG' 2>/dev/null)
echo "$monTestQuatre"
echo '------------------------------------------------------------------------'
echo 'TESTS UPLOAD KO'
echo '------------------------------------------------------------------------'
#Test : user ko, fichier existant et extension ok
curl -X POST -u "user:pwd" http://127.0.0.1:5000/uploadFile -F 'monFichier=@./testfiles/python.png'
#Test : user ok, fichier > 1Mo et extension ok
curl -X POST -u "benoitlarroque:mssio" http://127.0.0.1:5000/uploadFile -F 'monFichier=@./testfiles/bigimg.png'
#Test : user ok, fichier existant et extension ko
curl -X POST -u "benoitlarroque:mssio" http://127.0.0.1:5000/uploadFile -F 'monFichier=@./testfiles/data.sql'
echo '------------------------------------------------------------------------'
echo 'TESTS RECUPERATION FICHIER OK'
echo '------------------------------------------------------------------------'
#Test : user ok et identifiant fichier ok
curl -u "benoitlarroque:mssio" "http://127.0.0.1:5000/getfilebyid/$monTestUn"
echo''
curl -u "benoitlarroque:mssio" "http://127.0.0.1:5000/getfilebyid/$monTestDeux"
echo''
curl -u "benoitlarroque:mssio" "http://127.0.0.1:5000/getfilebyid/$monTestTrois"
echo''
curl -u "benoitlarroque:mssio" "http://127.0.0.1:5000/getfilebyid/$monTestQuatre"
echo''
echo '------------------------------------------------------------------------'
echo 'TESTS RECUPERATION FICHIER KO'
echo '------------------------------------------------------------------------'
#Test : user ko et identifiant fichier ok
curl -u "utilisateur:mdp" "http://127.0.0.1:5000/getfilebyid/$monTestUn"
#Test : user ko et identifiant ko
curl -u "utilisateur:mdp" "http://127.0.0.1:5000/getfilebyid/2020202049657678493"
#Test : user ok et identifiant ko
curl -u "benoitlarroque:mssio" "http://127.0.0.1:5000/getfilebyid/203494585GJFJ349EEF33"
echo '------------------------------------------------------------------------'
echo 'TESTS URL KO'
echo '------------------------------------------------------------------------'
curl -u "benoitlarroque:mssio" "http://127.0.0.1:5000/"
echo '------------------------------------------------------------------------'
echo 'FIN TESTS'
echo '------------------------------------------------------------------------'
