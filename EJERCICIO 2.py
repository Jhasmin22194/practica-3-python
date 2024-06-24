'''
Escribir un programa que gestione las calificaciones (calificaciones.csv) de los
estudiantes, el fichero debe contener: Ci, Apellido paterno, apellido materno, nombres,
primer parcial, segundo parcial, examen final.
• Crear el fichero si no existe
• Consultar las calificaciones de un estudiante
• Añadir un nuevo estudiante
• Eliminar el registro de un estudiante
• Mostrar sólo los estudiantes aprobados
• Mostrar la lista d estudiantes ordenado por apellido paterno
'''
import os
archivo='calificaciones.csv'
def crear_archivo():
    if not os.path.exists(archivo):
        with open(archivo, 'w') as file:
            pass
        print("Archivo de contactos creado.")
    else:
        print("El archivo de contactos ya existe.")
        
def añadir_estudiante(ci,pat,mat,nom,prim,seg,ter):
    try:
        with open(archivo,'a') as file:
            file.write(f"{ci}, {pat}, {mat}, {nom}, {prim}, {seg}, {ter}\n")
        print("Registro ingresado exitosamente")
    except FileNotFoundError:
        print("El archivo de contactos no existe.")

def consultar_calificaciones(est):
    try:
        no_encontrado=True
        with open(archivo,'r') as file:
            lineas=file.readlines()
            for linea in lineas:
                if linea[3].lower()==est.lower():
                    no_encontrado=False
                    print("Estudiante ",est," encontrado")
                    print("Primer parcial: ",linea[4])
                    print("Segundo parcial: ",linea[5])
                    print("Tercer parcial: ",linea[6])
        if no_encontrado:
            print("Estudiante no enontrado")
        
    except FileNotFoundError:
        print("El archivo de contactos no existe")

def eliminar_registro(ci):
    no_encontrado=True
    with open(archivo,'r') as file:
        lineas=file.readlines()
    with open(archivo,'w') as file:
        for linea in lineas:
            if linea[0] == ci.lower():
                no_encontrado=False
                print("Esta seguro de eliminar al estudiante S/N")
                res=input()
                if res.lower=='N':
                    break
            else:
                file.write(linea)
                encontrado = True
        if no_encontrado:
            print("Estudiante no encontrado")
                    
def mostrar_aprobados():
    pass
def mostrar_orenados():
    pass
    
def menu():
    print("Elige una opcion")
    print("1. Crear el fichero")
    print("2. Consultar las calificaciones de un estudiante")
    print("3. Añadir un nuevo estudiante")
    print("4. Eliminar el registro de un estudiante")
    print("5. Mostrar sólo los estudiantes aprobados")
    print("6. Mostrar la lista de estudiantes ordenado por apellido paterno")
    print("7. Salir")
    opc=int(input())
    return opc

# Crear el archivo
crear_archivo()

while (True):
    opc=menu()
    if opc == 1:
        crear_archivo()
    if opc == 2:
        nom=input("Nombre: ")
        num=input("Telefono: ")
        añadir_estudiante(nom,num)

    if opc == 3:
        ci=input("Cedula: ")
        pat=input("Apellido Paterno: ")
        mat=input("Apellido Materno: ")
        nom=input("Nombre: ")
        prim=float(input("Primer P: "))
        seg=float(input("Segundo P: "))
        ter=float(input("Tercer P: "))
        añadir_estudiante(ci,pat,mat,nom,prim,seg,ter)
    if opc == 4:
        ci=input("Ingrece la cedula del estudiante a eliminar")
    if opc == 5:
        pass
    if opc == 6:
        pass
    if opc == 7:
        break


