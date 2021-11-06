from flask import Flask


app = Flask(__name__)



@app.route('/')
def mostrar_tabla_movimientos():
    pass

@app.route('/purchase')
def mostrar_formulario_monedas():
    pass

@app.route('/status')
def mostrar_estado_inversion():
    pass
