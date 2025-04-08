# Lab - Deploy na Prática - App Web Para Previsão de Preço de Produtos
# app flask

# Imprts
from flask import Flask, request
from flask import render_template
from tools.entrega import Entrega

# Cria a app
app = Flask(__name__)

# Página de entrada
@app.route("/")
def index():
    result = None
    return render_template("index.html", result = result)

@app.route("/estimate", methods=["POST"])
def estimate():
    distancia = float(request.form['distancia'])
    if distancia > 20:
        return render_template('index.html', error="Distância não pode ser maior que 20 km.")

    # Extrai apenas a hora do campo tipo 'time'
    horario_str = request.form['horario']  # exemplo: '18:45'
    hora = int(horario_str.split(":")[0])  # pega só '18'

    # pega os outros valores
    values = [
        distancia,
        hora,
        float(request.form['valor_pedido']),
        float(request.form['pedidos_simultaneos']),
        float(request.form['clima']),
        float(request.form['congestionamento']),
    ]

    entrega = Entrega(values)
    value_to_predict = entrega.prepare()
    result = entrega.predict(value_to_predict)
    result = "%.2f" % result
    return render_template('index.html', result=result)

# Executa a app
if __name__ == "__main__":
    app.run(host = 'localhost', port = 3000, debug = True)
