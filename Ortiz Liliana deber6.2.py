from io import open

def guardar_estudiantes(nombre_archivo, estudiantes):
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            for estudiante in estudiantes.values():
                notas_str = ";".join(str(n) for n in estudiante["calificaciones"])
                archivo.write(f"{estudiante['cedula']},{estudiante['nombre']},{estudiante['edad']},{notas_str},{estudiante['promedio']:.2f}\n")
        print("Datos guardados correctamente.")
    except Exception as e:
        print("Error al guardar:", e)

def cargar_estudiantes(nombre_archivo):
    estudiantes = {}
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea:
                    partes = linea.split(",")
                    cedula = partes[0]
                    nombre = partes[1]
                    edad = int(partes[2])
                    calificaciones = list(map(float, partes[3].split(";")))
                    promedio = float(partes[4])
                    estudiantes[cedula] = {
                        "cedula": cedula,
                        "nombre": nombre,
                        "edad": edad,
                        "calificaciones": calificaciones,
                        "promedio": promedio
                    }
    except FileNotFoundError:
        print("Archivo no encontrado. Se inicia una base vacía.")
    return estudiantes

def calcular_promedio(notas):
    return round(sum(notas) / len(notas), 2)

def registrar_estudiante(estudiantes):
    print("\n--- Registrar estudiante ---")
    cedula = input("Cédula: ")
    if cedula in estudiantes:
        print("Ya existe un estudiante con esa cédula.")
        return
    nombre = input("Nombre: ")
    try:
        edad = int(input("Edad: "))
        calificaciones = []
        for i in range(5):
            nota = float(input(f"Ingrese nota {i+1}: "))
            calificaciones.append(nota)
    except ValueError:
        print("Error: entrada inválida.")
        return
    promedio = calcular_promedio(calificaciones)
    estudiantes[cedula] = {
        "cedula": cedula,
        "nombre": nombre,
        "edad": edad,
        "calificaciones": calificaciones,
        "promedio": promedio
    }
    guardar_estudiantes("estudiantes.txt", estudiantes)
    calcular_promedio_curso(estudiantes)

def calcular_promedio_curso(estudiantes):
    if not estudiantes:
        print("No hay estudiantes para calcular el promedio del curso.")
        return
    total = sum(e["promedio"] for e in estudiantes.values())
    promedio = total / len(estudiantes)
    print(f"Promedio general del curso: {promedio:.2f}")

def mostrar_ranking(estudiantes):
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    ordenados = sorted(estudiantes.values(), key=lambda e: e["promedio"], reverse=True)
    print("\n--- Ranking de estudiantes por promedio ---")
    for est in ordenados:
        print(f"{est['nombre']} ({est['cedula']}): {est['promedio']:.2f}")

    with open("ranking_estudiantes.txt", "w", encoding="utf-8") as archivo:
        for est in ordenados:
            archivo.write(f"{est['cedula']},{est['nombre']},{est['promedio']:.2f}\n")

def buscar_por_rango_edad(estudiantes):
    try:
        edad_min = int(input("Edad mínima: "))
        edad_max = int(input("Edad máxima: "))
    except ValueError:
        print("Edad no válida.")
        return
    print("\n--- Estudiantes en ese rango de edad ---")
    encontrados = [e for e in estudiantes.values() if edad_min <= e["edad"] <= edad_max]
    if encontrados:
        for e in encontrados:
            print(f"{e['nombre']} ({e['edad']} años) - Promedio: {e['promedio']:.2f}")
    else:
        print("No se encontraron estudiantes en ese rango.")

def actualizar_calificaciones(estudiantes):
    cedula = input("Cédula del estudiante a actualizar: ")
    if cedula not in estudiantes:
        print("Estudiante no encontrado.")
        return
    try:
        nuevas_notas = []
        for i in range(5):
            nota = float(input(f"Ingrese nueva nota {i+1}: "))
            nuevas_notas.append(nota)
    except ValueError:
        print("Error: notas inválidas.")
        return
    estudiantes[cedula]["calificaciones"] = nuevas_notas
    estudiantes[cedula]["promedio"] = calcular_promedio(nuevas_notas)
    print("Calificaciones actualizadas.")
    guardar_estudiantes("estudiantes.txt", estudiantes)

def mostrar_menu():
    print("\n--- MENÚ DEL SISTEMA ---")
    print("1. Registrar estudiante")
    print("2. Mostrar ranking por promedio")
    print("3. Buscar estudiantes por rango de edad")
    print("4. Actualizar calificaciones")
    print("5. Salir")

def main():
    archivo = "estudiantes.txt"
    estudiantes = cargar_estudiantes(archivo)
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_estudiante(estudiantes)
        elif opcion == "2":
            mostrar_ranking(estudiantes)
        elif opcion == "3":
            buscar_por_rango_edad(estudiantes)
        elif opcion == "4":
            actualizar_calificaciones(estudiantes)
        elif opcion == "5":
            guardar_estudiantes(archivo, estudiantes)
            print("Gracias por usar el sistema.")
            break
        else:
            print("RROR .")

main()
 