@echo off
echo Ajout des fichiers modifies...
git add .
echo Creation du commit...
git commit -m "Fix: photo Corinne Vignon ajoutée dans syndicats et chemin HTML corrigé"
echo Pousse vers le repertoire distant...
git push
echo.
echo Termine !
pause
