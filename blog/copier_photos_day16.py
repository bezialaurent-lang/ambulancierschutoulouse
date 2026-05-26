"""
Script à exécuter manuellement pour copier les photos du 26 Mai 2026
dans le dossier blog/photos/day16.

Usage: double-cliquez sur ce fichier ou exécutez dans un terminal:
    python copier_photos_day16.py
"""
import shutil
import os

src = os.path.join(os.path.dirname(__file__), '..', 'PHOTOS mobilisation', '26 Mai 2026')
dst = os.path.join(os.path.dirname(__file__), 'photos', 'day16')

os.makedirs(dst, exist_ok=True)

count = 0
for f in os.listdir(src):
    src_file = os.path.join(src, f)
    if os.path.isfile(src_file):
        shutil.copy2(src_file, os.path.join(dst, f))
        count += 1
        print(f"  Copié: {f}")

print(f"\nTerminé ! {count} fichiers copiés dans blog/photos/day16/")
input("Appuyez sur Entrée pour fermer...")
