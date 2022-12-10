import json
from flask import Flask, jsonify
import requests
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)

CORS(app)
app.secret_key = 'esto-es-una-clave-muy-secreta'

MONGO_URI = 'mongodb://db-mongo'

client = MongoClient(
            MONGO_URI,
            username= 'root',
            password='brayanyandru'
        )

db = client['chilet']
collection = db['celcius']

collection.insert_one({'name': 'Teclado'})
print('DB: ', db, flush=True)

@app.route("/")
def index():
    return jsonify({"name": "pong"})

@app.route('/nombres', methods=['GET'])
def name():
    return jsonify({"name": "Proyecto Alta Diponibilidad"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)