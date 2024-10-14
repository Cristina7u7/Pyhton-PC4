import random
from pyfiglet import Figlet

# Crear una instancia de Figlet
figlet = Figlet()

# Solicitar al usuario el nombre de una fuente
fuente = input("Ingrese el nombre de una fuente (o presione Enter para una fuente aleatoria): ")

# Obtener la lista de fuentes disponibles
fuentes_disponibles = figlet.getFonts()

# Si el usuario no ingresa una fuente, selecciona una aleatoria
if not fuente:
    fuente = random.choice(fuentes_disponibles)
else:
    if fuente not in fuentes_disponibles:
        print(f"La fuente '{fuente}' no está disponible. Se seleccionará una fuente aleatoria.")
        fuente = random.choice(fuentes_disponibles)

# Establecer la fuente seleccionada
figlet.setFont(font=fuente)

# Solicitar al usuario el texto a convertir en arte ASCII
texto = input("Ingrese el texto que desea convertir a arte ASCII: ")

# Mostrar el texto en arte ASCII
print(figlet.renderText(texto))