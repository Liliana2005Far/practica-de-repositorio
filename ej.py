from io import open

# Método que recibe el nombre del archivo como parámetro
def leerArchivo(archivo):
    try:
        with open(archivo, "r", encoding="utf-8") as archivo_texto:
            textoLineas = archivo_texto.readlines()
            return textoLineas
    except FileNotFoundError:
        print(f"Error: no se encontró el archivo {archivo}")
        return []
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return []

# Método corregido que ahora agrega (append) y no sobrescribe
def crearArchivo(archivo, informacion):
    try:
        with open(archivo, "a", encoding="utf-8") as archivo_texto:  # modo "a"
            archivo_texto.write(informacion + "\n")
            print("Información agregada al archivo exitosamente")
            return True
    except Exception as e:
        print("Error al tratar de agregar información al archivo")
        print(e)
        return False

# --- Uso del programa ---

# Leer archivo existente
datos = leerArchivo("notas.txt")
print("Información del archivo:")
for info in datos:
    print(info.strip())  # .strip() para evitar doble salto de línea

# Agregar una nueva línea al archivo de notas (sin eliminar lo anterior)
archivo = crearArchivo("notas.txt", "Notas del segundo Bimestre")
archivo = crearArchivo("notas.txt", "Notas del tercer Bimestre")