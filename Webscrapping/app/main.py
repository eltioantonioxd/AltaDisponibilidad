from dolar import getDolar
from uf import getUf
from temp import getTemp
from configdb import clientMongo
from insertData import insertOneDolar, insertOneUf, insertOneTemp

if "__main__" == __name__:
    print("Scrapping running")
    print("Loading data...")
    uf = getUf()
    dolar = getDolar()
    temp = getTemp()
    client = clientMongo()
    insertUf = insertOneUf(client, uf)
    insertDolar = insertOneDolar(client, dolar)
    insertTemp = insertOneTemp(client, temp)
    
    if insertUf == True and insertDolar == True and insertTemp == True:
        print('Inserción de datos realizada correctamente!')
    else:
        print('Error al insertar datos')
        
