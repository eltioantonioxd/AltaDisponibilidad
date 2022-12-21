from concurrent import futures
import grpc
from datetime import datetime
from pymongo import MongoClient
import myproto_pb2
import myproto_pb2_grpc
from time import time



MONGO_URI = 'mongodb://service-mongo.andrunose.svc.cluster.local'

client = MongoClient(
            MONGO_URI,
            username= 'root',
            password='brayanyandru'
        )

db = client['chilet']

def current_date_format(date):
    months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    day = date.day
    month = months[date.month - 1]
    year = date.year
    messsage = "{} de {} del {}".format(day, month, year)

    return messsage

now = datetime.now()
day = current_date_format(now)

class DataServer(myproto_pb2_grpc.Servicer):

    def GetTemperature(self, request, context):
        
        temperature= db['temperature'].find_one({'day': day})
        temperature={
            "id": str(temperature['_id']),
            "day": temperature['day'],
            "hours": temperature['hours'],
            "temp": temperature['temp']
        }
        temperature_response = myproto_pb2.TemperatureResponse(**temperature)

        return temperature_response


    def GetUF(self, request, context):
                
        uf = db['priceuf'].find_one({'day': day})
        
        data= {
            "id": str(uf['_id']),
            "day": uf['day'],
            "uf": uf['uf']
        }
        uf_response = myproto_pb2.UFResponse(**data)

        return uf_response


    def GetDollar(self, request, context):
                
        dollar = db['pricedolar'].find_one({'day': day})
        data= {
            "id": str(dollar['_id']),
            "day": dollar['day'],
            "dollar": dollar['dollar']
        }
        dollar_response = myproto_pb2.DollarResponse(**data)

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