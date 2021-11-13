# aqui poner las rutas y lo que hay que hacer en ellas

import time
import requests
from sqlite3.dbapi2 import Date
from flask import render_template, request, jsonify
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
        "to_quantity":""})

    if request.method == "POST":
    
        datos = {}
        mensaje = ""
        
        # OBTENGO EL DIA ACTUAL DEL SISTEMA
        datos["date"] = time.strftime("%y/%m/%d")
        # OBTENGO LA HORA ACTUAL DEL SISTEMA
        datos["time"] = time.strftime("%H:%M:%S")
        # UNO LOS DICCIONARIOS
        datos.update(request.form.to_dict())
        #  compruebo si el campo to_quantity esta vacio
        if datos["to_quantity"] == "":
            
            # COMPRUEBO QUE LOS DATOS INTRODUCIDOS NO SON LA MISMA MONEDA
            if datos["from_currency"] != datos["to_currency"]:
                # Llamada al api
                url = "https://rest.coinapi.io/v1/exchangerate/{from_currency}/{to_currency}?apikey={apikey}".format(
                    from_currency = datos["from_currency"],
                    to_currency = datos["to_currency"],
                    apikey=APIKEY)
                    
                tipo_cambio = requests.get(url)
                # guardo el resultado de rate en to_quantitty
                datos["to_quantity"] = float(tipo_cambio.json()["rate"]) * float(datos["from_quantity"])
            else:
                mensaje = f"Las monedas no pueden ser iguales"
        else:
            # convierto en tupla los valores del diccionario
            tupla = tuple(datos.values())
            db = Data_base(RUTA)
            # inserto los movimientos en base de datos
            resultado = db.insertarMovimiento(tupla)
            # compruebo si hubo error al crear el movimiento
            if resultado == True:
                mensaje = "Movimiento creado"
            else:
                mensaje = "Error al crear el movimiento"

        return render_template("purchase.html", mensaje=mensaje, datos=datos)