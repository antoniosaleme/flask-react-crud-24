from flask import Flask, request, jsonify
from flask_pymongo import PyMongo, ObjectId
from flask_cors import CORS

# Crear una instancia de la clase Flask
app = Flask(__name__)

# Configuración de la URI de MongoDB
app.config["MONGO_URI"] = "mongodb://localhost:27017/flask-react-crud"

# Inicializar PyMongo con la aplicación Flask
mongo = PyMongo(app)

users = mongo.db.users

@app.route('/users', methods=['POST'])
def createUser():
    id = users.insert_one({
        "name": request.json["name"],
        "email": request.json["email"],
        "password": request.json["password"]
    }).inserted_id 
    return jsonify(str(ObjectId(id)))
   

@app.route('/users', methods=['GET'])
def getUsers():
    usersList = []
    for doc in users.find():
        doc['_id'] = str(doc['_id'])
        usersList.append(doc)
    return jsonify(usersList)
    

@app.route('/users/<id>', methods=['GET'])
def getUser(id):
    user = users.find_one({"_id": ObjectId(id)})  # Convierte el id a ObjectId para la búsqueda
    if user:
        user['_id'] = str(user['_id'])  # Convierte el ObjectId a una cadena, porque objetId no es serializable
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/users/<id>', methods=['DELETE'])
def deleteUser():
    return "<h1>received</h1>"

@app.route('/users/<id>', methods=['PUT'])
def updateUser():
    return "<h1>received</h1>"

if __name__ == '__main__':
    app.run(port=5001, debug=True) # en true para que se reinicie el servidor cada vez que se haga un cambio en el código