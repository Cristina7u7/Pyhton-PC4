import requests

# Solicitar la cantidad de bitcoins
try:
    n = float(input("Indique la cantidad de bitcoins que posee: "))
except ValueError:
    print("Por favor, ingrese un número válido.")
    exit()

# Consultar el precio de Bitcoin usando la API de CoinDesk
url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

try:
    response = requests.get(url)
    response.raise_for_status()  # Verifica si la solicitud fue exitosa
    data = response.json()

    # Obtener el precio actual de Bitcoin en USD
    precio_bitcoin_usd = float(data['bpi']['USD']['rate'].replace(",", ""))

    # Calcular el costo en USD
    costo_total = n * precio_bitcoin_usd

    # Mostrar el costo total en formato de miles con 4 decimales
    print(f"El costo actual de {n} Bitcoins es: ${costo_total:,.4f} USD")

except requests.RequestException as e:
    print("Error al realizar la solicitud:", e)
except KeyError:
    print("No se puede obtener la información del precio.")