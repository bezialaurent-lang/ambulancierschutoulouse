import shutil
import os

src = os.path.join(r"c:\Users\MOI\Desktop\greve des ambulanciers", "article de presse", "la depeche 28-05-26.pdf")
dst = os.path.join(r"c:\Users\MOI\Desktop\greve des ambulanciers", "blog", "media", "la_depeche_28-05-26.pdf")

# Remove destination if it exists (in case of permission issue from partial copy)
if os.path.exists(dst):
    os.remove(dst)

shutil.copy2(src, dst)
print(f"Copie OK: {os.path.getsize(dst)} octets")
