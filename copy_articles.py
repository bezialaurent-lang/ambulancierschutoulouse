import shutil
import os

base_dir = r"c:\Users\MOI\Desktop\greve des ambulanciers"

articles = [
    "Lutte ouvriere CHU Toulouse \_ Ambulanciers hospitalier...pdf".replace(" \_", " _"),
    "Europe SAy _Des activités particulières et complex...pdf",
    "Grève des ambulanciers du CHU de Toulou...pdf",
    "Actu CHOLET Les ambulanciers du CHU de Toulouse en ...pdf"
]

src_dir = os.path.join(base_dir, 'article de presse')
dst_dir = os.path.join(base_dir, 'blog', 'media')

os.makedirs(dst_dir, exist_ok=True)

count = 0
for article in articles:
    src_file = os.path.join(src_dir, article)
    dst_file = os.path.join(dst_dir, article)
    if os.path.exists(src_file):
        try:
            shutil.copy2(src_file, dst_file)
            print(f"Copié : {article}")
            count += 1
        except Exception as e:
            print(f"Erreur copie {article} : {e}")
    else:
        print(f"Fichier non trouvé : {src_file}")

print(f"\n{count} articles copiés avec succès !")
input("Appuyez sur Entrée pour quitter...")
