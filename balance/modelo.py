from . import FICHERO
import csv


class Movimiento():
    def __init__(self, fecha, hora, concepto, ingreso_o_gasto, cantidad):
        self.fecha = fecha
        self.hora = hora
        self.concepto = concepto
        self.ingreso_gasto = ingreso_gasto
        self.cantidad = cantidad
        pass

class ListadoMovimientos():
    def __init__(self):
        self.movimientos=[]

    def leer_lista(self):
        with open(FICHERO, "r") as fichero:
            reader = csv.DictReader(fichero)
            for linea in reader:
                self.movimientos.append(linea)
