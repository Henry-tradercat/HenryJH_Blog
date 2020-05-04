import os
import secrets
from PIL import Image
from flask import current_app
from henryjh.models import About

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)
    i = Image.open(form_picture)
    i.save(picture_path)

    return picture_fn

def delete_picture():
    about = About.query.filter_by(id=1).first()
    prev_picture = os.path.join(current_app.root_path, 'static/profile_pics', about.image_file)
    if os.path.exists(prev_picture):
        os.remove(prev_picture)
