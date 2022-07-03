import os
from PIL import Image, ExifTags


img_folder = input(r"Enter the file path (e.g.:\"C:\Users\sureg\Desktop\nauka\python\public\exif_photos\pics\"): ")
img_contents = os.listdir(img_folder)
count = 0

def get_date():
    exif = {ExifTags.TAGS[k]: v for k, v in pil_img._getexif().items() if k in ExifTags.TAGS}
    global date
    date = {exif[k] for k in exif if k == 'DateTimeOriginal'}

def rename_file():
    new_path = os.path.join(img_folder, datetime)
    pil_img.close()
    os.rename(full_path, new_path) 

for image in img_contents:
    full_path = os.path.join(img_folder, image)
    pil_img = Image.open(full_path)
    try:
        get_date()
        new_date = str(date).replace(":", "").replace(" ", "-").replace("{", "").replace("}", "").strip("'")
        datetime = new_date + ".jpg" 
        rename_file()
    except FileExistsError:
        count += 1
        datetime = new_date + "-" + str(count) +".jpg"
        rename_file()
    except AttributeError:
        continue