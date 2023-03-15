from flask import jsonify, Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#decorador
@app.route('/')
def getHome():
    return jsonify({"message": "IPC2 los sobrevivientes"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)