import shutil
import os

base_dir = r"c:\Users\MOI\Desktop\greve des ambulanciers"
blog_dir = os.path.join(base_dir, "blog")

# 1. Copy article
src_article = os.path.join(base_dir, "article de presse", "depeche 10-06-26.pdf")
dst_article = os.path.join(blog_dir, "media", "depeche 10-06-26.pdf")

if os.path.exists(src_article):
    shutil.copy2(src_article, dst_article)
    print(f"Copied article: {dst_article}")
else:
    print(f"Error: article source not found at {src_article}")

# 2. Copy photos/videos for Day 23
src_photos = os.path.join(base_dir, "PHOTOS mobilisation", "10 juin 2026")
dst_photos = os.path.join(blog_dir, "photos", "day23")

os.makedirs(dst_photos, exist_ok=True)

if os.path.exists(src_photos):
    count = 0
    for f in os.listdir(src_photos):
        src_file = os.path.join(src_photos, f)
        if os.path.isfile(src_file):
            shutil.copy2(src_file, os.path.join(dst_photos, f))
            count += 1
            print(f"  Copied: {f}")
    print(f"Copied {count} media files for Day 23.")
else:
    print(f"Error: photos source not found at {src_photos}")

print("Done copying files for June 10.")
