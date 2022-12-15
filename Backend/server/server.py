from concurrent import futures
import grpc
from datetime import datetime
from pymongo import MongoClient
import myproto_pb2
import myproto_pb2_grpc
from time import time



MONGO_URI = 'mongodb://db-mongo'

client = MongoClient(
            MONGO_URI,
            username= 'root',
            password='brayanyandru'
        )

db = client['chilet']
collections = ['pricedolar','priceuf', 'temperature']
pricedolar = ['id', 'dolar', 'day']
priceuf = ['id', 'uf', 'day']
temperature = ['id', 'day', 'hours', 'temp']


class DataServer(myproto_pb2_grpc.Servicer):

    def GetTemperature(self, request, context):

        current_time = datetime.now()
        current_hour = current_time.hour

        temperature= db.temperature.find_one({'hours': {'$gte': current_hour}}, sort=[('hours', 1)])
        temperature={
            "id": "639937e9d862a52b17388d84",
            "day": "14 de Diciembre del 2022",
            "hours": [
            "02:00", "05:00",
            "08:00", "11:00",
            "14:00", "17:00",
            "20:00", "23:00"
            ],
            "temp": [
            "20°", "18°",
            "21°", "28°",
            "32°", "32°",
            "27°", "21°"
            ]
        }
        temperature_response = myproto_pb2.TemperatureResponse(**temperature)

        return temperature_response


    def GetUF(self, request, context):

        #fecha_hoy = datetime.date.today()
        #fecha_hoy_formateada = fecha_hoy.strftime("%d/%m/%Y")

        #uf= db.priceuf.find_one({'day': {'$gte': fecha_hoy}}, sort=[('day', 1)])
        uf= {
            "id": "639937e9d862a52b17388d84",
            "day": "14 de Diciembre del 2022",
            "uf": "30.000"
        }
        uf_response = myproto_pb2.UFResponse(**uf)

        return uf_response


    def GetDollar(self, request, context):
        
        fecha_hoy = datetime.date.today()
        
        dollar= db.pricedolar.find_one({'day': {'$gte': fecha_hoy}}, sort=[('day', 1)])
        dollar_response = myproto_pb2.DollarResponse(**dollar)

        return dollar_response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    myproto_pb2_grpc.add_ServicerServicer_to_server(DataServer(), server)
    server.add_insecure_port('[::]:50051')  
    server.start()
    server.wait_for_termination()
    #172.23.0.5
    
if __name__ == '__main__':
    serve()