@echo off
echo Copie des nouveaux logos de soutien...
copy /Y "..\soutien syndical\afash.jpg" "photos\syndicats\afash.jpg"
copy /Y "..\soutien syndical\logo-chru-tours.png" "photos\syndicats\logo-chru-tours.png"
copy /Y "..\soutien syndical\chu-angers-300x185.png" "photos\syndicats\chu-angers-300x185.png"
copy /Y "..\soutien syndical\CHU_de_Montpellier_(logo).svg.png" "photos\syndicats\CHU_de_Montpellier_(logo).svg.png"
copy /Y "..\soutien syndical\portrait carole delga.png" "photos\syndicats\portrait carole delga.png"
copy /Y "..\soutien syndical\lettre delga.jpeg" "media\lettre delga.jpeg"

echo Ajout des fichiers modifies...
git add .
echo Creation du commit...
git commit -m "Ajout du soutien de Carole Delga (portrait et lettre de soutien)"
echo Pousse vers le repertoire distant...
git push
echo.
echo Termine !
pause
