from flask import Flask



app = Flask(__name__)




@app.route('/')
def mostrar_tabla_movimientos():
    return " que tal"


@app.route('/purchase')
def mostrar_formulario_monedas():
    return "hasta luego"

@app.route('/status')
def mostrar_estado_inversion():
    pass
