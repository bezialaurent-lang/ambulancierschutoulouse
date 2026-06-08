import shutil
import os

base_dir = r"c:\Users\MOI\Desktop\greve des ambulanciers"

# Day 18 photos
src_photos = os.path.join(base_dir, 'PHOTOS mobilisation', '28 mai 2026')
dst_photos = os.path.join(base_dir, 'blog', 'photos', 'day18')

os.makedirs(dst_photos, exist_ok=True)
for f in os.listdir(src_photos):
    src_file = os.path.join(src_photos, f)
    if os.path.isfile(src_file):
        try:
            shutil.copy2(src_file, os.path.join(dst_photos, f))
            print(f"Copied {f}")
        except Exception as e:
            print(f"Failed to copy {f}: {e}")

# Communique
src_pdf = os.path.join(base_dir, 'communiqué', 'communique_presse_CHU_Toulouse27-05-26.pdf')
dst_pdf = os.path.join(base_dir, 'blog', 'media', 'communique_presse_CHU_Toulouse27-05-26.pdf')
try:
    shutil.copy2(src_pdf, dst_pdf)
    print("Copied PDF")
except Exception as e:
    print(f"Failed to copy PDF: {e}")
