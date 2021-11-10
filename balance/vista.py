# aqui poner las rutas y lo que hay que hacer en ellas
from flask import render_template, request
from . import app
from . import RUTA
from .modelo import Data_base, ListadoMovimientos

@app.route('/')
def mostrar_tabla():
    # PASAMOS RUTA
    db = Data_base(RUTA)
    # CONSULTAMOS MOVIMIENTOS
    movimientos = db.consultarSQL('SELECT * FROM MOVEMENTS')
    print(movimientos)
    #  render_template muestra la plantilla en pantalla, en este caso de inicio-html
    return render_template("inicio.html", movs=movimientos)



@app.route('/purchase', methods=["GET","POST"])
def mostrar_formulario():
    # COMPROBAR METODO GET O POST
    if request.method == "GET":
        return render_template('purchase.html')
    else:
        datos = request.form
        
        print(datos)
        return datos

# @app.route('/mostrar/<int:id>/<int:tipo>', methods=['GET','POST'])
# def actualizar_movimientos(id, tipo):
    # return f'Mostrando ficha de movimiento {id} y {tipo}'