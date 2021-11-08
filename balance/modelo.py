from datetime import date
from datetime import datetime
from . import FICHERO
import csv


class Movimiento():
    def __init__(self, linea):
        self.errores = []
        ahora = datetime.now()
        try:
            self.Fecha = date.fromisoformat(linea["Fecha"])
            if self.Fecha.strftime("%Y%m%d") > ahora.strftime("%Y%m%d"):
                self.errores.append("La fecha no puede ser futura")
                self.Fecha = "---"
        except ValueError:
            self.errores.append("Formato de fecha erroneo")
            self.Fecha = "XXX"
        self.Hora = linea["Hora"]
        self.From = linea["From"]
        self.Q = linea["Q"]
        self.To = linea["To"]
        pass

class ListadoMovimientos():
    def __init__(self):
        self.movimientos=[]

    def leer_lista(self):
        with open(FICHERO, "r") as fichero:
            reader = csv.DictReader(fichero)
            for linea in reader:
                movimiento=Movimiento(linea)
                self.movimientos.append(movimiento)
