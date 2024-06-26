'''
Crear un programa que lea un archivo de texto con el inventario de medicamentos de
una farmacia (nombre, cantidad disponible, precio unitario) y muestre en pantalla todos
los medicamentos con su respectiva información
'''
def crear():
    with open("inventario.txt", "w") as file:
        file.write("Nombre,Cantidad,Precio\n")
        print("Archivo creado exitosamente")

def agregar_medicamento():
    nombre = input("Ingrese el nombre del medicamento: ")
    cantidad = input("Ingrese la cantidad disponible: ")
    precio = input("Ingrese el precio unitario: ")
    with open("inventario.txt", "a") as file:
        file.write(f"{nombre},{cantidad},{precio}\n")
    print("Medicamento agregado exitosamente")

def mostrar():
    with open("inventario.txt", "r") as file:
        contenido = file.readlines()
        print("-" * 40)
        for linea in contenido:
            print(linea.replace(",", "\t"), end="")
        print("\n", "-" * 40)

while True:
    print("\tMENU DE OPCIONES")
    print("1. Crear el archivo")
    print("2. Agregar un medicamento")
    print("3. Mostrar inventario")
    print("4. Salir")
    opc = int(input())
    match opc:
        case 1:
            crear()
        case 2:
            agregar_medicamento()
        case 3:
            mostrar()
        case _:
            print("Hasta luego!!!.................")
            break
