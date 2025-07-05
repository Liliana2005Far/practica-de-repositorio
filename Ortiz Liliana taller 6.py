"""Adapta el código del CRUD visto en clase(Ejercicio de empleados) al siguiente ejercicio: 
Realice un programa que almacene la lista de empleados de una empresa. Todo el programa 
debe estar bajo un menú de opciones y trabajar con funciones.   """

from io import open

def guardar_personaje(personajes, archivo_nombre):
    try:
        with open(archivo_nombre, "w", encoding = "utf-8") as f:
            for emp in personajes:
                f.write(f"{emp['nombre']},{emp['anime']}, {emp['super poder']}, {emp['nivel poder']} \n")
        print("La informacion ha sido guardada en el archivo.")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

def registrar_datos(personajes):
    print("\n Vamos a registrar un nuevo personaje")
    nombre = input("Ingrese el nombre: ")
    anime = input("Ingrese el anime: ")
    super_poder=input("Ingrese el super poder: ")
    #Pedimos el nivel poder y lo validamos para asegurar que es un numero
    while True:
        try:
            nivel_poder = int(input("Ingrese el nivel-poder: "))
            break
        except ValueError:
            print("Nivel-poder no valido, ingrese un numero entero.")
    #Añadimos el nuevo nombre a la lista
    personajes.append({"nombre": nombre, "anime": anime, "super poder": super_poder, "nivel poder": nivel_poder})
    print("Se registro al empleado")
    calcular_promedio_nivel_poder(personajes)

def calcular_promedio_nivel_poder(personajes):
    #Calculo promedio nivel-poder todos los personajes
    if not personajes:
        print("No hay personajes para calcular promedio:")
        return 0
    #Sumanos todos los niveles de poder
    total_nivel_poder = sum(emp['nivel poder'] for emp in personajes)
    #Calcular promedio
    promedio = total_nivel_poder/len(personajes)
    print(f"El promedio de los niveles de poder de los personajes es: {promedio:.2f}")
    return promedio

def mostrar_info_ordenada(personajes):
    #Muestra info personajes ordenados alfabeticamente por nombre y guarda en otro archivo
    if not personajes:
        print("No hay personajes para mostrar")
        return
    #Crear una copia ordenada de la lista para no alterar la original
    personajes_ordenados = sorted(personajes, key = lambda emp:emp['nivel poder'])
    print("Informacion ordenada de los personajes por orden ascendente-------")
    #Imprimimos la lista ordenada
    for emp in personajes_ordenados:
        print(f"Nombre: {emp['nombre']}, Anime: {emp['anime']}, Super poder: {emp['super poder']}, Nivel poder: {emp['nivel poder']}")
    #Guardamos esta lista ya ordenada en otro archivo
    guardar_personaje(personajes_ordenados,'personajes_ordenados_nivel.txt')

def buscar_personaje_por_nombre(personajes):
    if not personajes:
        print("No hay personajes para mostrar")
        return
    
    nombre_busqueda =input("\nIngrese el nombre a buscar: ")
    #Buscamos en la listado los personajes que cumplen criterio
    #Comprension de lista
    encontrados = [emp for emp in personajes if emp ['nombre'] == nombre_busqueda]
    
    if encontrados:
        print(f"Personajes con nombre  {nombre_busqueda}")
        for emp in encontrados:
            print(f"Nombre: {emp['nombre']}, Anime: {emp['anime']}, Super poder: {emp['super poder']}, Nivel poder: {emp['nivel poder']}")
    else:
        print("No se encontraron personajes con ese nivel de poder. ")

def mostrar_menu():
    print("\nMenu de opciones")
    print("1.Registrar datos de los Personajes")
    print("2.Mostrar informacion en orden ascendente por nivel de poder.")
    print("3.Buscar personaje por nombre")
    print("4.Salir")

def cargar_datos(archivo_nombre):
    personajes = []
    try:
        with open(archivo_nombre, "r", encoding = "utf-8") as archivo_texto:
            for linea in archivo_texto:
                linea = linea.strip() #Elimina saltos de linea
                if linea: #La linea no esta vacia
                    nombre, anime, super_poder, nivel_poder = linea.split(",")
                    personajes.append({"nombre": nombre,"anime": anime, "super poder":super_poder, "nivel poder": int(nivel_poder)})
        return personajes
    except FileNotFoundError:
        print("El archivo no existe")
        return[]
    
def main():
    nombre_archivo = "personajes anime.txt"
    nombre_archivo2 = "personajes anime ordenados.txt"
    lista_personajes = cargar_datos(nombre_archivo)
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")
        if opcion == '1':
            registrar_datos(lista_personajes)
            guardar_personaje(lista_personajes, nombre_archivo)
        elif opcion == '2':
            mostrar_info_ordenada(lista_personajes)
        elif opcion == '3':
            buscar_personaje_por_nombre(lista_personajes)
        elif opcion == '4':
            guardar_personaje(lista_personajes,nombre_archivo)
            print("Programa finalizado")
            break;
        else:
            print("Opcion no valida, Intente de nuevo")

main()