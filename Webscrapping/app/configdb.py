from pymongo import MongoClient

def clientMongo():
    try:
        MONGO_URI = 'mongodb://182.160.26.111'
        client = MongoClient(
                    MONGO_URI,
                    username= 'root',
                    password='brayanyandru'
                )
        return client
    
    except ConnectionError as error:
        return error