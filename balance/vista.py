# aqui poner las rutas y lo que hay que hacer en ellas

from . import app
from .modelo import ListadoMovimientos

@app.route('/')
def mostrar_tabla():
    lista_movimientos = ListadoMovimientos()
    lista_movimientos.leer_lista()
    return lista_movimientos.movimientos