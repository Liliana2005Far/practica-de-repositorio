'''
Realice un programa que almacene la lista de empleados de una empresa. Todo el programa debe estar bajo un menú de opciones y trabajar con funciones.  
Registrar datos de los empleados: nombre, cedula y sueldo. Calcular el promedio de los sueldos. (Guardar la información en un archivo)
Mostrar la información en orden alfabético en consola (Guardar la información en un archivo)
Buscar un empleado por sueldo.
Salir
'''
from io import open
def guardar_empleados(empleados, archivo_nombre):
    #Cada empleado se guarda en una linea con formato nombre cedula y sueldo
    try:
        with open(archivo_nombre, "w", encoding = "utf-8") as f:
            for emp in empleados:
                f.write(f"{emp['nombre']},{emp['cedula']}, {emp['sueldo']} \n")
        print("La informacion ha sido guardada en el archivo.")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

def registrar_datos(empleados):
    print("\n Vamos a registrar un nuevo empleado")
    nombre = input("Ingrese el nombre: ")
    cedula = input("Ingrese la cedula: ")
    #Pedimos el sueldo y lo validamos para asegurar que es un numero
    while True:
        try:
            sueldo = float(input("Ingrese el sueldo: "))
            break
        except ValueError:
            print("Sueldo no valido, ingrese un numero.")
    #Añadimos el nuevo empleado a la lista
    empleados.append({"nombre": nombre, "cedula": cedula, "sueldo": sueldo})
    print("Se registro al empleado")
    calcular_promedio_sueldos(empleados)

def calcular_promedio_sueldos(empleados):
    #Calculo promedio sueldo todos los empleados
    if not empleados:
        print("No hay empleados para calcular promedio:")
        return 0
    #Sumanos todos los sueldos
    total_sueldos = sum(emp['sueldo'] for emp in empleados)
    #Calcular promedio
    promedio = total_sueldos/len(empleados)
    print(f"El promedio de los sueldos es: {promedio:.2f}")
    return promedio
def mostrar_info_ordenada(empleados):
    #Muestra info empleados ordenados alfabeticamente por nombre y guarda en otro archivo
    if not empleados:
        print("No hay empleados para mostrar")
        return
    #Crear una copia ordenada de la lista para no alterar la original
    empleados_ordenados = sorted(empleados, key = lambda emp:emp['nombre'])
    print("Informacion ordenada de empleados por orden alfabetico-------")
    #Imprimimos la lista ordenada
    for emp in empleados_ordenados:
        print(f"Nombre: {emp['nombre']}, Cedula: {emp['cedula']}. Sueldo: ${emp['sueldo']:.2f}")
    #Guardamos esta lista ya ordenada en otro archivo
    guardar_empleados(empleados_ordenados,'empleados_ordenados.txt')

def buscar_empleado_por_sueldo(empleados):
    if not empleados:
        print("No hay empleados para mostrar")
        return
    while True:
        try:
            sueldo_busqueda = float(input("\nIngrese el sueldo a buscar"))
            break
        except ValueError:
            print("Sueldo no valido, por favor ingrese un numero. ")
    #Buscamos en la listado los empleados que cumplen criterio
    #Comprension de lista
    encontrados = [emp for emp in empleados if emp ['sueldo'] == sueldo_busqueda]
    #forma tradicional
    # encontrados = []
    # for emp in empleados:
    #     if emp['sueldo'] == sueldo_busqueda:
    #         encontrados.append(emp)
    if encontrados:
        print(f"Empleados con sueldo ${sueldo_busqueda:.2f}")
        for emp in encontrados:
            print(f"Nombre: {emp['nombre']}, Cedula: {emp['cedula']}, Sueldo: ${emp['sueldo']:.2f}")
    else:
        print("No se encontraron empleados con ese sueldo: ")

def mostrar_menu():
    print("\nMenu de opciones")
    print("1.Registrar datos de los Empleados")
    print("2. Mostrar informacion en orden alfabetico y guardar en el archivo")
    print("3. Buscar empleado por sueldo")
    print("4.Salir")
def cargar_datos(archivo_nombre):
    empleados = []
    try:
        with open(archivo_nombre, "r", encoding = "utf-8") as archivo_texto:
            for linea in archivo_texto:
                linea = linea.strip() #Elimina saltos de linea
                if linea: #La linea no esta vacia
                    nombre, cedula, sueldo = linea.split(",")
                    empleados.append({"nombre": nombre,"cedula": cedula, "sueldo": float(sueldo)})
        return empleados
    except FileNotFoundError:
        print("El archivo no existe")
        return[]

def main():
    nombre_archivo = "empleados.txt"
    nombre_archivo2 = "empleados_ordenados.txt"
    lista_empleados = cargar_datos(nombre_archivo)
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")
        if opcion == '1':
            registrar_datos(lista_empleados)
            guardar_empleados(lista_empleados, nombre_archivo)
        elif opcion == '2':
            mostrar_info_ordenada(lista_empleados)
        elif opcion == '3':
            buscar_empleado_por_sueldo(lista_empleados)
        elif opcion == '4':
            guardar_empleados(lista_empleados,nombre_archivo)
            print("Programa finalizado")
            break;
        else:
            print("Opcion no valida, Intente de nuevo")

main()