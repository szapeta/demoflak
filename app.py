from flask import jsonify, Flask, request
from flask_cors import CORS
import doble
import Pila

app = Flask(__name__)
CORS(app)

miPila = Pila.Pila()

#decorador
@app.route('/') #<- se intica el tipo de peticion, default get
def getHome():
    return jsonify({"message": "IPC2 los sobrevivientes"})


@app.route('/', methods=['POST'])  
def confi():
    if request.method == 'POST':
        numero = request.form['valor']
        respuesta = doble.getDoble(int(numero))
        return jsonify({"el doble es:": respuesta})

@app.route('/agregar', methods=['POST'])  
def agregar():
    if request.method == 'POST':
        numero = request.json['valorjson']
        respuesta = doble.getDuplicado(numero)
        return jsonify({"Texto duplicado:": respuesta})

@app.route('/addPila', methods=['POST'])     
def addPila():
    if request.method == 'POST':
        valorLeido = request.form['valor']
        miPila.insertar(valorLeido)
        return jsonify({"msg": "ok"})
    
@app.route('/getPila')  
def getPila():
    return jsonify({"pila": miPila.printPila()})

if __name__ == '__main__':
    app.run(debug=True, port=5000)