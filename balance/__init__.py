# INICIAMOS FLASK
from flask import Flask

FICHERO = "balance/data/movimientos.csv"

app = Flask(__name__)

from . import vista
