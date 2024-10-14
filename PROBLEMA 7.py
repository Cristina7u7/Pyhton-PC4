import requests
import sqlite3
from datetime import datetime

# URL de la API de la SUNAT
url_sunat = "https://api.apis.net.pe/v1/tipo-cambio-sunat"

# Realizar la solicitud a la API
try:
    response = requests.get(url_sunat)
    response.raise_for_status()  # Verifica si la solicitud fue exitosa
    tipo_cambio_data = response.json()

    # Extraer los valores de la API
    fecha = tipo_cambio_data['fecha']
    compra = tipo_cambio_data['compra']
    venta = tipo_cambio_data['venta']
    
    # Mostrar los datos obtenidos
    print(f"Fecha: {fecha}, Compra: {compra}, Venta: {venta}")
    
except requests.RequestException as e:
    print(f"Error al obtener datos de la API: {e}")
    exit()

# Conectar a la base de datos SQLite o crearla si no existe
conexion = sqlite3.connect('base.db')
cursor = conexion.cursor()

# Crear la tabla sunat_info si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sunat_info (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha TEXT,
        compra REAL,
        venta REAL
    )
''')

# Insertar los datos en la tabla sunat_info
try:
    cursor.execute('''
        INSERT INTO sunat_info (fecha, compra, venta)
        VALUES (?, ?, ?)
    ''', (fecha, compra, venta))

    # Guardar los cambios en la base de datos
    conexion.commit()
    print("Datos insertados en la base de datos.")

except sqlite3.Error as e:
    print(f"Error al insertar datos en la base de datos: {e}")
    conexion.rollback()

# Mostrar los datos almacenados en la tabla
try:
    cursor.execute('SELECT * FROM sunat_info')
    filas = cursor.fetchall()

    print("\nContenido de la tabla sunat_info:")
    for fila in filas:
        print(f"ID: {fila[0]}, Fecha: {fila[1]}, Compra: {fila[2]}, Venta: {fila[3]}")
    
except sqlite3.Error as e:
    print(f"Error al leer la base de datos: {e}")

# Cerrar la conexión
conexion.close()