# aqui poner las rutas y lo que hay que hacer en ellas

import time
from sqlite3.dbapi2 import Date
from flask import render_template, request
from . import app
from . import RUTA, APIKEY
from .modelo import Data_base

@app.route('/')
def mostrar_tabla():
    db = Data_base(RUTA)
    movimientos = db.consultarSQL('SELECT * FROM MOVEMENTS')
    print(movimientos)
    #  render_template muestra la plantilla en pantalla, en este caso de inicio-html
    return render_template("inicio.html", movs=movimientos)

    
@app.route('/purchase', methods=["GET","POST"])
def mostrar_formulario():

    # COMPROBAR METODO GET O POST
    if request.method == "GET":
        return render_template('purchase.html', datos={
        "from_currency":"",
        "from_quantity":"",
        "to_currency":"",
        "to_quantity":""}
        )
    
    if request.method == "POST":
        datos = {}
        datos["date"] = time.strftime("%y/%m/%d")
        datos["time"] = time.strftime("%H:%M:%S")
        datos.update(request.form.to_dict())
        if datos["from_currency"] == datos["to_currency"]:
            return f"los valores no pueden ser iguales"
        else:
        # print(datos["from_currency"])
        # print(datos["to_currency"])
            tupla = tuple(datos.values())
            print(tupla)
            db = Data_base(RUTA)
            resultado = db.insertarMovimiento(tupla)
            #resultado = False
            return render_template("purchase.html",
            resultado=resultado,
            datos=datos.values())


        
        
        
        
        
        
        
        
        
        
        
        
        # url = "https://rest.coinapi.io/v1/exchangerate/{from_currency}/{to_currency}?ap"ikey={apikey}".format(
        # from_currency = datos['from_currency'],
        # to_currency = datos['to_currency'],
        # apikey = APIKEY)

        #if len(nmov.errores) > 0:
        #    return render_template("purchase.html", errores=nmov.errores, datos=datos)

  
  