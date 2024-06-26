'''
Realice el programa para crear el archivo, “menu.txt”, guardar registros y mostrar la
información guardada en el mismo.
Menú
Número Nombre Tipo Precio
1 Plato Paceño A 15
2 Plato Paceño B 20
3 Picante Mixto A 40
4 Trucha ahumada A 35
'''
def crear():
    with open("menu.txt", "w") as file:
        file.write("Numero,Nombre,Tipo,Precio\n")
        print("Archivo creado exitosamente")

def agregar_plato():
    numero = input("Ingrese el número del plato: ")
    nombre = input("Ingrese el nombre del plato: ")
    tipo = input("Ingrese el tipo del plato: ")
    precio = input("Ingrese el precio del plato: ")
    with open("menu.txt", "a") as file:
        file.write(f"{numero},{nombre},{tipo},{precio}\n")
    print("Plato agregado exitosamente")

def mostrar():
    with open("menu.txt", "r") as file:
        contenido = file.readlines()
        print("-" * 40)
        for linea in contenido:
            print(linea.replace(",", "\t"), end="")
        print("\n", "-" * 40)

while True:
    print("\tMENU DE OPCIONES")
    print("1. Crear el archivo")
    print("2. Agregar un plato")
    print("3. Mostrar menú")
    print("4. Salir")
    opc = int(input())
    match opc:
        case 1:
            crear()
        case 2:
            agregar_plato()
        case 3:
            mostrar()
        case _:
            print("Hasta luego!!!.................")
            break
