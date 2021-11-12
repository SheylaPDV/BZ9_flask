# aqui poner las rutas y lo que hay que hacer en ellas

import time
from sqlite3.dbapi2 import Date
from flask import render_template, request
from . import app
from . import RUTA, APIKEY
from .modelo import Data_base

@app.route('/')
def mostrar_tabla():
    # CREO EL OBJETO DB CON LA RUTA DE LA BASE DE DATOS
    db = Data_base(RUTA)
    # MOVIMIENTOS ES TODOS LOS MOVMIMENTOS AL CONSULTAR LA BASE DE DATOS
    movimientos = db.consultarSQL('SELECT * FROM MOVEMENTS')
    #  IMPRMIMO TODOS LOS MOVMIMENOS
    print(movimientos)
    # RENDER TEMPLATE MUESTRA TODOS LOS MOVMIMENTOS EN LA PAGINA DE INICIO
    return render_template("inicio.html", movs=movimientos)

    
@app.route('/purchase', methods=["GET","POST"])
def mostrar_formulario():

    #COMPRUEBO SI EL METODO GET O POST
    if request.method == "GET":
        return render_template('purchase.html', datos={
        "from_currency":"",
        "from_quantity":"",
        "to_currency":"",
        "to_quantity":""}
        )
    
    if request.method == "POST":

        datos = {}
        mensaje = ""
        # OBTENGO EL DIA ACTUAL DEL SISTEMA
        datos["date"] = time.strftime("%y/%m/%d")
        # OBTENGO LA HORA ACTUAL DEL SISTEMA
        datos["time"] = time.strftime("%H:%M:%S")
        # UNO LOS DICCIONARIOS
        datos.update(request.form.to_dict())
        # COMPRUEBO QUE LOS DATOS INTRODUCIDOS NO SON LA MISMA MONEDA
        if datos["from_currency"] == datos["to_currency"]:
            mensaje = "Los monedas no pueden ser iguales"
        # SI SON DISTINTAS LAS MONEDAS, AÑADO EL MOVIMIMENTO A LA BASE DE DATOS
        else:
            # GUARDO EN UNA TUPLA TODOS LOS VALORES
            tupla = tuple(datos.values())
            db = Data_base(RUTA)
            # INSERTO EL MOVIMIENTO EN BASE DE DATOS
            resultado = db.insertarMovimiento(tupla)
            # COMPRUEBO EL RESULTADO DE INSERTAR EN LA BASE DE DATOS
            if resultado == True:
                mensaje = "Movimiento creado"
            else:
                mensaje = "Error al crear el movimiento"
            # if datos["to_quantity"] == None:
                # url = f"https://rest.coinapi.io/v1/exchangerate/{"from_currency"}/{to_currency}?apikey={APIKEY}";

        
        return render_template("purchase.html", mensaje=mensaje, datos=datos)


        
        
        
        
        
        
        
        
        
        
        
        
        # url = "https://rest.coinapi.io/v1/exchangerate/{from_currency}/{to_currency}?apikey={apikey}".format(
        # from_currency = datos['from_currency'],
        # to_currency = datos['to_currency'],
        # apikey = APIKEY)

        #if len(nmov.errores) > 0:
        #    return render_template("purchase.html", errores=nmov.errores, datos=datos)

  
  