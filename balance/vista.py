# aqui poner las rutas y lo que hay que hacer en ellas
from flask import render_template, request
from . import app
from .modelo import ListadoMovimientos

@app.route('/')
def mostrar_tabla():
    lista_movimientos = ListadoMovimientos()
    lista_movimientos.leer_lista()
    #return lista_movimientos.movimientos
    #  render_template muestra la plantilla en pantalla, en este caso de inicio-html

    return render_template("inicio.html", movs=lista_movimientos.movimientos)

@app.route('/compra', methods=["GET","POST"])
def mostrar_formulario():
    # COMPROBAR METODO GET O POST
    # if request.method == "GET":
    return render_template("compra.html")
    # else:
        # datos = request.form
        # return datos
