from flask import Flask
from project.helpers.remove_bg import image
import os

app = Flask(__name__)


app.register_blueprint(image, url_prefix ="/image")