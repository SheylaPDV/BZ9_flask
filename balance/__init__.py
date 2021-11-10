# INICIAMOS FLASK
from flask import Flask

RUTA = 'balance/data/movements.db'

app = Flask(__name__)

from . import vista
