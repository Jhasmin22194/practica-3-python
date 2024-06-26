'''
Escribir un programa que gestione los datos de empleados de una empresa en el archivo
“empleados.txt”, que tiene los siguientes datos: nombre, apellido paterno y edad.
Escribir funciones que permitan crear el archivo, modificar información del archivo y
eliminar algún dato del archivo.
'''
def crear():
    with open("empleados.txt","w") as file:
        file.write("ID,Nombre,Apellido,Edad\n")
        print("Archivo creado exitosamente")
        pass

def modificar():
    idmod=input("Ingrese el id: ")
    with open("empleados.txt","r") as file:
        cont=file.readlines()
    with open("empleados.txt","w") as file:
        for linea in cont:
            pal=linea.strip().split(",")
            if pal[0] == idmod:
                while(True):
                    print("Datos encontrados")
                    print("1. Modificar nombre")
                    print("2. Modificar apellido")
                    print("3. Modificar edad")
                    print("4. Finalizar modificacion")
                    opc=int(input())
                    match opc:
                        case 1:
                            pal[1]=input("Nuevo nombre: ")
                        case 2:
                            pal[2]=input("Nuevo apellido: ")
                        case 3:
                            pal[3]=input("Nueva edad: ")
                        case _:
                            break
                n_linea=",".join(pal)+"\n"
                linea.replace("linea",n_linea)
                file.write(n_linea)
                print("Datos actualizados................")
                    
            else:
                file.write(linea)
                
def eliminar():
    idmod=input("Ingrese el id: ")
    with open("empleados.txt","r") as file:
        cont=file.readlines()
    with open("empleados.txt","w") as file:
        sw=0
        for linea in cont:
            pal=linea.strip().split(",")
            if pal[0] == idmod:
                res=input("Esta seguro de seguir S/N: ")
                if res.upper()=="S":
                    sw=1
                    print("Registro eliminado................")
                else:
                    file.write(linea)
                    print("Proceso cancelado.............")
            else:
                file.write(linea)
        if sw==0:
            print("Dato no encontrado")
            
def registrar():
    empleado=[input("Ingrese el id: "),input("Ingrese el nombre del empleado: "),input("Ingrese el apellido paterno: "),input("Ingrese la edad del empleado: ")]
    with open("empleados.txt","a") as file:
        file.write(",".join(empleado)+"\n")
        print("Datos registrados exitosamente")

def mostrar():
    with open("empleados.txt","r") as file:
        contenido=file.readlines()
        print("-"*40)
        for linea in contenido:
            print(linea.replace(",","\t"), end="")
        print("\n","-"*40)

while (True):
    print("\t MENU DE OPCIONES")
    print("1. Crear el archivo")
    print("2. Registrar nuevo empleados")
    print("3. Modificar un empleado")
    print("4. Eliminar un empleado")
    print("5. Mostrar empleados")
    print("6. Salir")
    opc=int(input())
    match opc:
        case 1:
            crear()
        case 2:
            registrar()
        case 3:
            modificar()
        case 4:
            eliminar()
        case 5:
            mostrar()
        case _:
            print("Hasta luego!!!.................")
            break