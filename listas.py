import requests
_ENDPOINT = "https://api.binance.com"

def url(api):
    return _ENDPOINT+api

def get_price(cripto):
    return requests.get(url("/api/v3/ticker/price?symbol="+cripto))

def esmoneda(cripto):
    criptos = ["BTC","BCC","LTC","ETH","ETC","XRP"]
    if cripto in criptos:
        return True
    else:
        return False

def esnumero(numero): 
    return numero.replace('.','',1).isdigit()

monedas = []
cantidades = []
cotizaciones = []
i = 0
while i < 3:
    moneda = input("Ingrese nombre de la moneda : ")
    while not esmoneda(moneda):
        print("no es una moneda valida")
        moneda = input("Ingrese nombre de la moneda : ")
    else:
        monedas.append(moneda)
        date = get_price(moneda+"USDT").json()
        cotizaciones.append(float(date["price"]))
        cantidad = input("Ingrese la cantidad de "+moneda+" : ")
        while not esnumero(cantidad):
            cantidad = input("indique la cantidad de "+moneda+" :")
        else:
            cantidades.append(float(cantidad))
    i+=1
i = 0
total = 0.0
while i<3:
    total+= cantidades[i]*cotizaciones[i]
    print("Moneda: ",monedas[i],
        " Cantidad: ",cantidades[i],
        " Cotizaciones: ",cotizaciones[i],
        " cantidad de USDT: ",cantidades[i]*cotizaciones[i])
    i+=1
print("total USDT es: ",str(total))