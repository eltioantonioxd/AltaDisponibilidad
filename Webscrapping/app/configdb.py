from pymongo import MongoClient

def clientMongo():
    try:
        MONGO_URI = 'mongodb://service-mongo.andrunose.svc.cluster.local'
        client = MongoClient(
                    MONGO_URI,
                    username= 'root',
                    password='brayanyandru'
                )
        return client
    
    except ConnectionError as error:
        return error