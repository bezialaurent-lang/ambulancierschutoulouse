@echo off
echo Ajout des fichiers modifies...
git add .
echo Creation du commit...
git commit -m "Fix: uniformise la taille du logo PS avec celui de LFI"
echo Pousse vers le repertoire distant...
git push
echo.
echo Termine !
pause
