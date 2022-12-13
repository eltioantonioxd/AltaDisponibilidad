import json
from flask import Flask, jsonify
import requests
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)

CORS(app)
app.secret_key = 'esto-es-una-clave-muy-secreta'

@app.route("/")
def index():
    return jsonify({"name": "pong"})

@app.route('/nombres', methods=['GET'])
def name():
    return jsonify({"name": "Proyecto Alta Diponibilidad"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)