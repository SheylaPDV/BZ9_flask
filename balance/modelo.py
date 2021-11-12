import sqlite3
from datetime import date
from datetime import datetime

# CREAMOS CONEXION A BASE DE DATOS
class Data_base:
    def __init__(self, ruta):
        self.ruta = ruta

    def consultarSQL(self, consulta):  
        conexion = sqlite3.connect(self.ruta)
        cursor = conexion.cursor()
        cursor.execute(consulta)
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
        conexion.close()
        return self.movimientos


    def insertarMovimiento(self, movimiento):
        conexion = sqlite3.connect(self.ruta)
        cursor = conexion.cursor()
        resultado = False
        try:
            consulta = "INSERT INTO MOVEMENTS (date,time,from_currency,from_quantity,to_currency,to_quantity) VALUES(?,?,?,?,?,?);"
            cursor.execute(consulta, movimiento)
            conexion.commit()
            resultado = True
        except:
            conexion.rollback()
        conexion.close()
        print("Resultado:", resultado)
        return resultado


















"""
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
   
