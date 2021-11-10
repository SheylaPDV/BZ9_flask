import sqlite3
from datetime import date
from datetime import datetime
#from . import FICHERO
import csv

# SELECT fecha, hora, from_quantity FROM MOVEMENTS
# CREAMOS CONEXION A BASE DE DATOS
class Data_base:
    def __init__(self, ruta):
        self.ruta = ruta

    def consultarSQL(self, consulta):  
        # CONECTO CON LA BASE DE DATOS
        conexion = sqlite3.connect(self.ruta)
        # ABRO EL CURSOR
        cursor = conexion.cursor()
        # EJECUTO SENTENCIA SQL
        cursor.execute(consulta)
        # GUARDO
        conexion.commit()

        self.movimientos = []
        nombre_columnas = []
        for tupla in cursor.description:
            nombre_columnas.append(tupla[0])

        datos = cursor.fetchall()

        for tupla in datos:
            mov = {}
            indice = 0
            for nombre in nombre_columnas:
                mov[nombre]=tupla[indice]
                indice += 1
            self.movimientos.append(mov)
        # CIERRO CONEXION
        conexion.close()
        return self.movimientos


class Movimiento():
    def __init__(self, linea):
        # LISTA VACIA DE ERRORES EN CASO DE QUE LOS HAYA
        self.errores = []
        # DATETIME.NOW TE SACA LA FECHA ACTUAL
        ahora = datetime.now()
        try:
            # EVALUAR SI HAY ERRORES EN LA FECHA
            self.Fecha = date.fromisoformat(linea["Fecha"])
            if self.Fecha.strftime("%Y%m%d") > ahora.strftime("%Y%m%d"):
                self.errores.append("La fecha no puede ser futura")
                self.Fecha = "---"
        except ValueError:
            # SI HAY ERRORES,  AÑADE A LA LISTA VACIA DE ERRORES "FORMATO DE FECHA ERRONEO"
            self.errores.append("Formato de fecha erroneo")
            # Y TE PINTA EN LA CASILLA DE FECHA 3 X, PARA SABER QUE NO VALE
            self.Fecha = "XXX"
            # LEE CADA LINEA DE MOVMIMENTOS.CSV
        self.Hora = linea["Hora"]
        self.From = linea["From"]
        self.QF = linea["Q"]
        self.To = linea["To"]
        self.QT = linea["Q"]
        pass

class ListadoMovimientos():
    def __init__(self):
        # LISTA VACIA DONDE SE INTRODUCEN LOS MOVIMIENTOS
        self.movimientos=[]

    """
    def leer_lista(self):
        # ABRIMOS FICHERO (ESTA METIDO EN LA VARIABLE FICHERO EN INIT)
        with open(FICHERO, "r") as fichero:
            # CONVIERTE FICHERO EN UN DICCIONARIO
            reader = csv.DictReader(fichero)
            # BUCLE PARA LEER POR LINEA EL FICHERO
            for linea in reader:
                # PORCADA LINEA SE AÑADE EN FORMA DE DICCIONARIO EN LISTA VACIA MOVIMIENTOS
                movimiento=Movimiento(linea)
                self.movimientos.append(movimiento)
    """
