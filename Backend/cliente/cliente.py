from flask import Flask, request
import grpc
import json
from google.protobuf.json_format import MessageToJson
from flask import request, jsonify
from flask_cors import CORS
import myproto_pb2
import myproto_pb2_grpc

app = Flask(__name__)
CORS(app)

app.secret_key = 'esto-es-una-clave-muy-secreta'

class DataClient:
    def __init__(self):
       
        self.channel = grpc.insecure_channel('service-servidor.andrunose.svc.cluster.local:50051', options=(('grpc.enable_http_proxy', 0),))
        self.stub = myproto_pb2_grpc.ServicerStub(self.channel)

    def get_temperature(self):
        request = myproto_pb2.Empty()
        return self.stub.GetTemperature(request)

    def get_uf(self):
        request = myproto_pb2.Empty()
        return self.stub.GetUF(request)

    def get_dollar(self):
        request = myproto_pb2.Empty()
        return self.stub.GetDollar(request)


@app.route('/temperature', methods=['GET'])
def get_temperature():
    if request.method == 'GET':
        client = DataClient()
        response = client.get_temperature()
        response = MessageToJson(response)
        response = json.loads(response)
        return jsonify(response)

@app.route('/uf', methods=['GET'])
def get_uf():
    if request.method == 'GET':
        client = DataClient()
        response = client.get_uf()
        response = MessageToJson(response)
        response = json.loads(response)
        return jsonify(response)

@app.route('/dollar', methods=['GET'])
def get_dollar():
    if request.method == 'GET':
        client = DataClient()
        response = client.get_dollar()
        response = MessageToJson(response)
        response = json.loads(response)
        return jsonify(response)

@app.route('/crossword', methods=['GET'])
def get_crossword_link():
    if request.method == 'GET':
        url = 'https://www.tarkus.info/movil/crucigrama.php?nomm=Crucigrama&nom=10/12/2022&crucigrama=8QnijP3s7QUsDDn0vzYIcZ76oBUVfYbFeXbQRd15u9Y='
        response = {'crucigrama': url}
    return response

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)