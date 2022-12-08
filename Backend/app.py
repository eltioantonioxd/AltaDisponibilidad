import json
from flask import Flask, jsonify
import requests
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


app.config["MONGO_URI"] = "mongodb://localhost:27017/chilet"
mongo = PyMongo(app)

url = 'https://www.freetogame.com/api/games'
data = requests.get(url)
data = data.json()

app.secret_key = 'esto-es-una-clave-muy-secreta'

@app.route("/")
def index():
    return jsonify({"name": "pong"})

@app.route('/nombres', methods=['GET'])
def name():
    return jsonify({"name": "Brayan Espina Tramolao"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)