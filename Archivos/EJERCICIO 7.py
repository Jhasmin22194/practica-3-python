'''
Crear un programa que lea un archivo de texto con la lista de niños inscritos en un centro
infantil (nombre, edad, nombre del padre/madre) y muestre en pantalla todos los niños
con su respectiva información
'''

def crear():
    with open("ninos.txt", "w") as file:
        file.write("Nombre,Edad,Nombre del Padre/Madre\n")
        print("Archivo creado exitosamente")

def agregar_nino():
    nombre = input("Ingrese el nombre del niño: ")
    edad = input("Ingrese la edad del niño: ")
    nombre_padre_madre = input("Ingrese el nombre del padre/madre: ")
    with open("ninos.txt", "a") as file:
        file.write(f"{nombre},{edad},{nombre_padre_madre}\n")
    print("Niño agregado exitosamente")

def mostrar():
    with open("ninos.txt", "r") as file:
        contenido = file.readlines()
        print("-" * 40)
        for linea in contenido:
            print(linea.replace(",", "\t"), end="")
        print("\n", "-" * 40)

while True:
    print("\tMENU DE OPCIONES")
    print("1. Crear el archivo")
    print("2. Agregar un niño")
    print("3. Mostrar lista de niños")
    print("4. Salir")
    opc = int(input())
    match opc:
        case 1:
            crear()
        case 2:
            agregar_nino()
        case 3:
            mostrar()
        case _:
            print("Hasta luego!!!.................")
            break
