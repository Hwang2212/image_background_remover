from rembg import remove
from PIL import Image
from flask import Flask, Blueprint, request, jsonify, send_file
from werkzeug.utils import secure_filename
import os



image = Blueprint('image', '__name__')

@image.route("/remove_bg", methods = ["POST"])
def remove_bg():
    file = request.files['image']
    file.save(os.path.join("/Users/artisan/Test/project/temp",secure_filename(file.filename)))
    # file.save(secure_filename(file.filename))
    # img = file.save(secure_filename(file.filename))
    img = Image.open(os.path.join("/Users/artisan/Test/project/temp",secure_filename(file.filename)))
    output = remove(img)
    if os.path.exists(os.path.join("/Users/artisan/Test/project/temp",secure_filename(file.filename))):
        os.remove(os.path.join("/Users/artisan/Test/project/temp",secure_filename(file.filename)))
    else:
        print("The file does not exist")
    output.save(os.path.join("/Users/artisan/Test/project/temp","test.png"))
    return send_file(os.path.join("/Users/artisan/Test/project/temp","test.png"))
