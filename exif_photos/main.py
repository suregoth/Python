import os
from PIL import Image, ExifTags

img_folder = r"C:\Users\sureg\Desktop\nauka\python\public\exif_photos\pics"
img_contents = os.listdir(img_folder)


for image in img_contents:
    full_path = os.path.join(img_folder, image)
    # ext = os.path.splitext(image)[1]
    pil_img = Image.open(full_path)
    exif = {ExifTags.TAGS[k]: v for k, v in pil_img._getexif().items() if k in ExifTags.TAGS}
    date = {exif[k] for k in exif if k == 'DateTimeOriginal'}
    datetime = str(date).replace(":", "").replace(" ", "-").replace("{", "").replace("}", "").strip("'") + ".jpg"
    new_path = os.path.join(img_folder, datetime)
    pil_img.close()
    os.rename(full_path, new_path)