from dolar import getDolar
from uf import getUf
from temp import getTemp

if "__main__" == __name__:
    print("Scrapping running")
    print("Loading data...")
    uf = getUf()
    dolar = getDolar()
    temp = getTemp()
    print('valor uf actual: ', uf)
    print('valor dolar actual:', dolar)
    print('valor temperatura:', temp)
