import os
from PIL import Image
from flask import url_for,current_app

def add_profile_pic(profile_pic,username):

    filename=profile_pic.filename
    ext=filename.split('.')[-1]
    storage_filename=str(username)+'.'+ext
    filepath=os.path.join(current_app.root_path,'static/profile_pics',storage_filename)
    output_size=(200,200)

    pic=Image.open(profile_pic)
    pic.thumbnail(output_size)
    pic.save(filepath)

    return storage_filename