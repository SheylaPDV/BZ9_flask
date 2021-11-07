from flask import Flask

FICHERO = "data/movimientos.csv"

app = Flask(__name__)

from . import vista
