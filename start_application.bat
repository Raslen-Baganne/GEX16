@echo off
echo Demarrage de l'application Gexpertise7...

echo 1. Demarrage du service de dossiers (folder_service.py)...
start cmd /k "cd /d %~dp0Backend && python folder_service.py"
timeout /t 5

echo 2. Demarrage du serveur backend principal...
start cmd /k "cd /d %~dp0Backend && python app.py"
timeout /t 5

echo 3. Demarrage du frontend...
start cmd /k "cd /d %~dp0Frontend && npm start"

echo Tous les services ont ete demarres!
echo Pour arreter les services, fermez les fenetres de terminal ouvertes.
