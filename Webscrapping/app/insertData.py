
def insertOneDolar(client, data):
    try:
        db = client['chilet']
        collection = db['pricedolar']
        collection.insert_one(data)
        return True
    except ConnectionError as error:
        return error

def insertOneUf(client, data):
    try:
        db = client['chilet']
        collection = db['priceuf']
        collection.insert_one(data)
        return True
    except ConnectionError as error:
        return error
    
def insertOneTemp(client, data):
    try:
        db = client['chilet']
        collection = db['temperature']
        collection.insert_one(data)
        return True
    except ConnectionError as error:
        return error
