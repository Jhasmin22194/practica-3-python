'''
Crear un programa que lea un archivo de texto con registros de personas (nombre,
apellido paterno, cédula de identidad) y muestre en pantalla todos los registros y permita
buscar a una persona por su cédula de identidad.
'''
def crear():
    with open("emp.txt","w") as file:
        file.write("Nombre,Apellido,Cedula\n")
        print("Archivo creado exitosamente")
        pass

def buscar():
    idmod=input("Ingrese la cedula: ")
    with open("emp.txt","r") as file:
        cont=file.readlines()
    with open("emp.txt","w") as file:
        for linea in cont:
            pal=linea.strip().split(",")
            if pal[2] == idmod:
                file.write(linea)
                print("Datos encontrados..............")
                print("Nombre: ",pal[0])
                print("Apellido: ",pal[1])
                print("Cedula: ",pal[2])
                    
            else:
                file.write(linea)
                

def mostrar():
    with open("emp.txt","r") as file:
        contenido=file.readlines()
        print("-"*40)
        for linea in contenido:
            print(linea.replace(",","\t"), end="")
        print("\n","-"*40)

while (True):
    print("\t MENU DE OPCIONES")
    print("1. Crear el archivo")
    print("2. Buscar un empleado")
    print("3. Mostrar empleados")
    print("4. Salir")
    opc=int(input())
    match opc:
        case 1:
            crear()
        case 2:
            buscar()
        case 3:
            mostrar()
        case _:
            print("Hasta luego!!!.................")
            break