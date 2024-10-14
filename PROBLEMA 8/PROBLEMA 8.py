import csv
import sqlite3

# Conectar a la base de datos SQLite
conexion = sqlite3.connect('base.db')
cursor = conexion.cursor()

# Función para obtener el tipo de cambio (venta) por fecha desde la base de datos
def obtener_tipo_cambio(fecha):
    cursor.execute("SELECT venta FROM sunat_info WHERE fecha = ?", (fecha,))
    resultado = cursor.fetchone()
    if resultado:
        return resultado[0]  # Retorna el tipo de cambio de venta
    else:
        return None

# Leer el archivo CSV de ventas
with open('ventas.csv', 'r') as archivo_csv:
    lector_csv = csv.DictReader(archivo_csv)
    
    # Variables para almacenar el total en dólares y en soles
    total_dolares = 0
    total_soles = 0
    
    # Recorrer cada fila del archivo CSV
    for fila in lector_csv:
        producto = fila['producto']
        fecha = fila['fecha']
        precio_usd = float(fila['precio_usd'])
        
        # Obtener el tipo de cambio para la fecha de la venta
        tipo_cambio = obtener_tipo_cambio(fecha)
        
        if tipo_cambio:
            # Calcular el precio en soles
            precio_soles = precio_usd * tipo_cambio
            
            # Sumar al total
            total_dolares += precio_usd
            total_soles += precio_soles
            
            # Mostrar el precio del producto en dólares y soles
            print(f"Producto: {producto}, Fecha: {fecha}, Precio en USD: ${precio_usd:.2f}, Precio en soles: S/{precio_soles:.2f}")
        else:
            print(f"No se encontró el tipo de cambio para la fecha {fecha}.")

# Mostrar el total en dólares y soles
print(f"\nTotal en USD: ${total_dolares:.2f}")
print(f"Total en soles: S/{total_soles:.2f}")

# Cerrar la conexión a la base de datos
conexion.close()