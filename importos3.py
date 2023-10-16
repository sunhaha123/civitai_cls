from pathlib import Path
import imghdr
import os

data_dir = "/root/autodl-tmp/20k/aesthetics_20000/"
image_extensions = [".png", ".jpg"]  # add there all your images file extensions

img_type_accepted_by_tf = ["bmp", "gif", "jpeg", "png"]
for filepath in Path(data_dir).rglob("*"):
    if filepath.suffix.lower() in image_extensions:
        img_type = imghdr.what(filepath)
        if img_type is None:
            os.remove(filepath)
            print(f"{filepath} is not an image")
        elif img_type not in img_type_accepted_by_tf:
            os.remove(filepath)
            print(f"{filepath} is a {img_type}, not accepted by TensorFlow")