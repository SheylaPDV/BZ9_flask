# aqui poner las rutas y lo que hay que hacer en ellas
from flask import render_template, request
from . import app
from . import RUTA, APIKEY
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
        return render_template('purchase.html', datos={"date":"", "time":"", "from_currency":"", "from_quantity":"", "to_currency":"", "to_quantity":""} )
    
    if request.method == "POST":
        datos = request.form.to_dict()
        # url = "https://rest.coinapi.io/v1/exchangerate/{from_currency}/{to_currency}?ap"ikey={apikey}".format(
        # from_currency = datos['from_currency'],
        # to_currency = datos['to_currency'],
        # apikey = APIKEY)
        tupla = tuple(datos.values())
        print(tupla)
        db = Data_base(RUTA)
        resultado = db.insertarMovimiento(tupla)
        #if len(nmov.errores) > 0:
        #    return render_template("purchase.html", errores=nmov.errores, datos=datos)
        return render_template("purchase.html", resultado=resultado, datos=datos.values())
        

  
  