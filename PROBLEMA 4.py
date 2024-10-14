import csv

# Inicializar variables para almacenar los datos
temperaturas = []
archivo_entrada = 'temperaturas.txt'
archivo_salida = 'resumen_temperaturas.txt'

# Leer el archivo CSV
try:
    with open(archivo_entrada, 'r') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        next(lector_csv)  # Saltar la cabecera (fecha,temperatura)
        
        for fila in lector_csv:
            try:
                temperatura = float(fila[1])  # Convertir el valor de temperatura a float
                temperaturas.append(temperatura)
            except ValueError:
                print(f"Advertencia: No se pudo procesar el valor de temperatura en la fila: {fila}")

except FileNotFoundError:
    print(f"Error: No se encontró el archivo {archivo_entrada}")
    exit()

# Calcular estadísticas
if temperaturas:
    temperatura_maxima = max(temperaturas)
    temperatura_minima = min(temperaturas)
    temperatura_promedio = sum(temperaturas) / len(temperaturas)

    # Escribir los resultados en un nuevo archivo
    try:
        with open(archivo_salida, 'w') as archivo_resumen:
            archivo_resumen.write(f"Temperatura máxima: {temperatura_maxima:.2f}°C\n")
            archivo_resumen.write(f"Temperatura mínima: {temperatura_minima:.2f}°C\n")
            archivo_resumen.write(f"Temperatura promedio: {temperatura_promedio:.2f}°C\n")
        print(f"Resultados escritos en {archivo_salida}")

    except Exception as e:
        print(f"Error al escribir en el archivo: {e}")
else:
    print("No se encontraron datos de temperatura.")