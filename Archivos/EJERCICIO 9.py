'''
Cree un programa para manejar un archivo correspondiente a la venta de ropa e
identifique al menos 3 campos, y realice los módulos correspondientes para guardar
información en el archivo “ventas.txt”, y leer la información correspondiente guardada.
'''
def crear():
    with open("ventas.txt", "w") as file:
        file.write("ID,Artículo,Cantidad,Precio\n")
        print("Archivo creado exitosamente")

def agregar_venta():
    id_venta = input("Ingrese el ID de la venta: ")
    articulo = input("Ingrese el nombre del artículo: ")
    cantidad = input("Ingrese la cantidad vendida: ")
    precio = input("Ingrese el precio del artículo: ")
    with open("ventas.txt", "a") as file:
        file.write(f"{id_venta},{articulo},{cantidad},{precio}\n")
    print("Venta agregada exitosamente")

def mostrar_ventas():
    with open("ventas.txt", "r") as file:
        contenido = file.readlines()
        print("-" * 40)
        for linea in contenido:
            print(linea.replace(",", "\t"), end="")
        print("\n", "-" * 40)

while True:
    print("\tMENU DE OPCIONES")
    print("1. Crear el archivo")
    print("2. Agregar una venta")
    print("3. Mostrar ventas")
    print("4. Salir")
    opc = int(input())
    match opc:
        case 1:
            crear()
        case 2:
            agregar_venta()
        case 3:
            mostrar_ventas()
        case _:
            print("Hasta luego!!!.................")
            break
