@echo off
echo Ajout des fichiers modifies...
git add .
echo Creation du commit...
git commit -m "Ajout communique mobilisation 19 juin 2026, compteur 401241, et equilibrage des logos de soutiens"
echo Pousse vers le repertoire distant...
git push
echo.
echo Termine !
pause
