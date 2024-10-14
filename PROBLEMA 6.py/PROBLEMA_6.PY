import os

def contar_lineas_codigo(ruta_archivo):
    # Imprimir la ruta ingresada para depuración
    print(f"Ruta del archivo ingresada: {ruta_archivo}")
    
    # Verificar si el archivo existe y si es un archivo .py
    if not os.path.exists(ruta_archivo):
        print(f"Error: El archivo {ruta_archivo} no existe.")
        return
    if not ruta_archivo.endswith('.py'):
        print("Error: El archivo no es un archivo Python (.py).")
        return

    try:
        # Abrir el archivo en modo lectura
        with open(ruta_archivo, 'r') as archivo:
            lineas = archivo.readlines()

        # Contar las líneas de código, excluyendo comentarios y líneas en blanco
        lineas_codigo = 0
        for linea in lineas:
            linea_limpia = linea.strip()
            if linea_limpia and not linea_limpia.startswith("#"):
                lineas_codigo += 1

        print(f"Número de líneas de código en {ruta_archivo}: {lineas_codigo}")
    
    except Exception as e:
        print(f"Error al leer el archivo: {e}")

# Solicitar la ruta del archivo al usuario
ruta_archivo = input("Ingrese la ruta del archivo .py: ")
contar_lineas_codigo(ruta_archivo)