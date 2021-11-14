import sqlite3

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