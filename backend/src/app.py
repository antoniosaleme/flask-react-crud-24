from flask import Flask, request
from flask_pymongo import PyMongo
from flask_cors import CORS

# Crear una instancia de la clase Flask
app = Flask(__name__)

# Configuración de la URI de MongoDB
app.config["MONGO_URI"] = "mongodb://localhost:27017/flask-react-crud"

# Inicializar PyMongo con la aplicación Flask
mongo = PyMongo(app)

db = mongo.db.users

@app.route('/users', methods=['POST'])
def createUser():
    print(request.json)
    return "<h1>received</h1>"

@app.route('/users', methods=['GET'])
def getUsers():
    return "<h1>received</h1>"

@app.route('/users/<id>', methods=['GET'])
def getUser():
    return "<h1>received</h1>"

@app.route('/users/<id>', methods=['DELETE'])
def deleteUser():
    return "<h1>received</h1>"

@app.route('/users/<id>', methods=['PUT'])
def updateUser():
    return "<h1>received</h1>"

if __name__ == '__main__':
    app.run(port=5001, debug=True) # en true para que se reinicie el servidor cada vez que se haga un cambio en el código