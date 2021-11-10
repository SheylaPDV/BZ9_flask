# INICIAMOS FLASK
from flask import Flask

RUTA = 'balance/data/movements.db'
APIKEY = '80CDBBD8-8C86-42DA-BA3F-499D14C79045'

app = Flask(__name__)

from . import vista
