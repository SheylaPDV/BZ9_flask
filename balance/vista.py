# aqui poner las rutas y lo que hay que hacer en ellas

from . import app

@app.route('/')
def mostrar_tabla():
    return "ya estaos aqui"