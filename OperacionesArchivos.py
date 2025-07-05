#ARCHIVOS
from io import open
#  Metodo que recibe el nombre dek archivo como parametro
def leerArchivo(archivo):
    #  iniciamos un bloque try para manejar posibles errores
    try:
        #abrimos el archivo en modo lectura ("r")
        #  el with garantiza que el archivo se cierre automaticamente
        with open(archivo, "r", encoding="utf-8") as archivo_texto:
            #   leeemos TODAS las lineas del archivo y las guardamos en una lista
            textoLineas=archivo_texto.readlines()
            #   retornamos la lista con todas las lineas procesadas
            return textoLineas
        #   capturamos el error de archivo no encontrado
    except FileNotFoundError:
        # mostramos un mensaje de error especifico
        print(f"Error: no se encontro el archivo{archivo}")
        # retornamos una lista vacia para evitar errores en el codigo que llamamos
        return []
    
    # capramos cualquier otro tipo de error
    except Exception as e:
        # mostramos el error especifico que ocurrio
        print(f"Error al leer el archivo: {e}")
        #retornamos una lista vacia
        return []
    
    def crearArchivo(archivo, informacion):
        try:
            # abrimos el archivo que nos pasaron
            # "w" significa que lo creamos si no existe, o lo vaciamos si ya existe (truncamos)
            # tambien le decimos que use UTF-8 para que entienda tildes y eñes
            with open(archivo, "a", encoding="utf-8") as archivo_texto:
                # escribimos la INFO que recibimos y añadimos un salto de linea.
                archivo_texto.write(informacion+"\n")
                print("Archivo creado o modificado exitosamente")
                # y devolvemos True para indicar que funciono
                return True
            # pero si algo falta
        except Exception as e:
            #Imprimimos un mensaje de error generico
            print("Error al tratar de crear o modificar el archivo")
            # Y mostramos el error especifico que ocurrio (por ejemplo: permiso denegado).
            print(e)
            # Devolvemos False para indicar que falto
            return False
        
        #from OperacionesArchivos import *

# Leer archivo existente
datos = leerArchivo("animes.txt")
print("Información del archivo:")
for info in datos:
    print(info.strip())  # .strip() para evitar doble salto de línea


# Agregar una nueva línea al archivo de notas (sin eliminar lo anterior)
archivo= crearArchivo("C:/Users/juanc/Desktop/notas.txt", "Notas del segundo Bimestre")

