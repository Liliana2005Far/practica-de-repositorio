from io import open

def cargar_inventario(nombre_archivo):
    inventario = []
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            for linea in f:
                datos = linea.strip().split(",")
                if len(datos) == 4:
                    codigo, nombre, precio, cantidad = datos
                    inventario.append([codigo, nombre, float(precio), int(cantidad)])
    except FileNotFoundError:
        print("No se encontró el archivo, se iniciará un inventario vacío.")
    return inventario

def guardar_inventario(nombre_archivo, inventario):
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        for prod in inventario:
            f.write(f"{prod[0]},{prod[1]},{prod[2]},{prod[3]}\n")

def registrar_producto(inventario):
    codigo = input("Ingrese el código: ")
    nombre = input("Ingrese el nombre: ")
    while True:
        try:
            precio = float(input("Ingrese el precio: "))
            cantidad = int(input("Ingrese la cantidad: "))
            break
        except ValueError:
            print("Error: Ingrese valores numéricos válidos para precio y cantidad.")

    inventario.append([codigo, nombre, precio, cantidad])
    guardar_inventario("inventario.txt", inventario)
    print("Producto registrado exitosamente.")
    calcular_valor_total(inventario)

def calcular_valor_total(inventario):
    total = sum(prod[2] * prod[3] for prod in inventario)
    print(f"\nValor total del inventario: ${total:.2f}")

def mostrar_inventario_ordenado(inventario):
    if not inventario:
        print("El inventario está vacío.")
        return

    ordenado = sorted(inventario, key=lambda x: x[2])  # orden por precio
    print("\n--- Inventario ordenado por precio (menor a mayor) ---")
    for prod in ordenado:
        print(f"Código: {prod[0]}, Nombre: {prod[1]}, Precio: ${prod[2]:.2f}, Cantidad: {prod[3]}")
    guardar_inventario("inventario_ordenado.txt", ordenado)

def buscar_por_rango_precio(inventario):
    try:
        minimo = float(input("Ingrese el precio mínimo: "))
        maximo = float(input("Ingrese el precio máximo: "))
    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")
        return

    resultados = [p for p in inventario if minimo <= p[2] <= maximo]
    if resultados:
        print(f"\nProductos entre ${minimo:.2f} y ${maximo:.2f}:")
        for p in resultados:
            print(f"Código: {p[0]}, Nombre: {p[1]}, Precio: ${p[2]:.2f}, Cantidad: {p[3]}")
    else:
        print("No se encontraron productos en ese rango.")

def actualizar_cantidad_producto(inventario):
    codigo = input("Ingrese el código del producto a actualizar: ")
    for prod in inventario:
        if prod[0] == codigo:
            print(f"Producto encontrado: {prod[1]}, Cantidad actual: {prod[3]}")
            try:
                nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
                prod[3] = nueva_cantidad
                guardar_inventario("inventario.txt", inventario)
                print("Cantidad actualizada correctamente.")
            except ValueError:
                print("Error: debe ingresar un número entero.")
            return
    print("No se encontró ningún producto con ese código.")

def mostrar_menu():
    print("\n--------- MENÚ DE INVENTARIO ---------")
    print("1. Registrar producto")
    print("2. Mostrar inventario ordenado por precio")
    print("3. Buscar productos por rango de precio")
    print("4. Actualizar cantidad de producto")
    print("5. Salir")

def main():
    archivo = "inventario.txt"
    inventario = cargar_inventario(archivo)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            registrar_producto(inventario)
        elif opcion == '2':
            mostrar_inventario_ordenado(inventario)
        elif opcion == '3':
            buscar_por_rango_precio(inventario)
        elif opcion == '4':
            actualizar_cantidad_producto(inventario)
        elif opcion == '5':
            print("Gracias por usar el sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

# Ejecutar el programa
main()
