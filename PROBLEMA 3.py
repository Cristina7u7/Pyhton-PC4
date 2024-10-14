import requests
import zipfile
import os

# Descargar la imagen
url_imagen = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
nombre_imagen = "imagen_descargada.jpg"

# Realizamos la descarga de la imagen
try:
    print("Descargando la imagen...")
    respuesta = requests.get(url_imagen)
    respuesta.raise_for_status()  # Verifica si la solicitud fue exitosa

    # Guardamos la imagen en un archivo local
    with open(nombre_imagen, 'wb') as archivo_imagen:
        archivo_imagen.write(respuesta.content)
    print("Imagen descargada con éxito.")
    
except requests.RequestException as e:
    print(f"Error al descargar la imagen: {e}")

# Comprimir la imagen en un archivo ZIP
nombre_zip = "imagen_comprimida.zip"
try:
    with zipfile.ZipFile(nombre_zip, 'w') as archivo_zip:
        archivo_zip.write(nombre_imagen)
    print(f"Imagen comprimida en el archivo {nombre_zip}")
    
except Exception as e:
    print(f"Error al comprimir la imagen: {e}")

# Descomprimir el archivo ZIP
try:
    with zipfile.ZipFile(nombre_zip, 'r') as archivo_zip:
        archivo_zip.extractall("imagen_extraida")
    print(f"Imagen extraída en la carpeta 'imagen_extraida'")
    
except Exception as e:
    print(f"Error al descomprimir el archivo: {e}")