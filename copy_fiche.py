import shutil
import os

base_dir = r"c:\Users\MOI\Desktop\greve des ambulanciers"

src_file = os.path.join(base_dir, 'reglementation', 'Ambulancier(ère)_A0055.pdf')
dst_dir = os.path.join(base_dir, 'blog', 'media')
dst_file = os.path.join(dst_dir, 'Ambulancier_A0055.pdf')

os.makedirs(dst_dir, exist_ok=True)

if os.path.exists(src_file):
    try:
        shutil.copy2(src_file, dst_file)
        print("Copié avec succès !")
    except Exception as e:
        print(f"Erreur copie : {e}")
else:
    print(f"Fichier non trouvé : {src_file}")

input("Appuyez sur Entrée pour quitter...")
