from datetime import date
from datetime import datetime
from . import FICHERO
import csv


class Movimiento():
    def __init__(self, linea):
        self.errores = []
        ahora = datetime.now()
        try:
            self.fecha = date.fromisoformat(linea["fecha"])
            if self.fecha.strftime("%Y%m%d") > ahora.strftime("%Y%m%d"):
                self.errores.append("La fecha no puede ser futura")
        except ValueError:
            self.errores.apend("Formato de fecha erroneo")
        self.hora = linea["hora"]
        self.concepto = linea["concepto"]
        self.ingreso_gasto = linea["ingreso_gasto"]
        self.cantidad = linea["cantidad"]
        pass

class ListadoMovimientos():
    def __init__(self):
        self.movimientos=[]

    def leer_lista(self):
        with open(FICHERO, "r") as fichero:
            reader = csv.DictReader(fichero)
            for linea in reader:
                self.movimientos.append(linea)
