# aqui poner las rutas y lo que hay que hacer en ellas

from . import app
from .modelo import ListadoMovimientos

@app.route('/')
def mostrar_tabla():
    movimientos = ListadoMovimientos()
    return "ya estaos aqui"