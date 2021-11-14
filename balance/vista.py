import time
import requests
from sqlite3.dbapi2 import Date
from flask import render_template, request
from . import app
from . import RUTA, APIKEY
from .modelo import Data_base

@app.route('/')
def mostrar_tabla():
    # creo el objeto db con la ruta de la base de datos
    db = Data_base(RUTA)
    # todos los movimientos al consultlar la base de datos
    movimientos = db.consultarSQL('SELECT * FROM MOVEMENTS')
    # muestra todos los movimientos en la pagina de inicio
    return render_template("inicio.html", movs=movimientos)

    
@app.route('/purchase', methods=["GET","POST"])
def mostrar_formulario():

    #compruebo si el metodo es get o post
    if request.method == "GET":
        return render_template('purchase.html', datos={
        "from_currency":"",
        "from_quantity":"",
        "to_currency":"",
        "to_quantity":""})

    if request.method == "POST":
    
        datos = {}
        mensaje = ""
        
        # obtengo el dia actual del sistema
        datos["date"] = time.strftime("%y/%m/%d")
        # obtengo la hora actual del sistema
        datos["time"] = time.strftime("%H:%M:%S")
        # uno los diccionarios
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