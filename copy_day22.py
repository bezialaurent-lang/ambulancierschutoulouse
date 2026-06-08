import os
import shutil

src = r"c:\Users\MOI\Desktop\greve des ambulanciers\PHOTOS mobilisation\01 Juin 2026"
dst = r"c:\Users\MOI\Desktop\greve des ambulanciers\blog\photos\day22"

if not os.path.exists(dst):
    os.makedirs(dst)

for item in os.listdir(src):
    s = os.path.join(src, item)
    d = os.path.join(dst, item)
    if os.path.isdir(s):
        shutil.copytree(s, d, dirs_exist_ok=True)
    else:
        shutil.copy2(s, d)
        
print("Copied successfully.")
