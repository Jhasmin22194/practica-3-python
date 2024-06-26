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

def consultar_calificaciones(ci):
    try:
        no_encontrado=True
        with open(archivo,'r') as file:
            lineas=file.readlines()
            for linea in lineas:
                palabra=linea.strip().split(",")
                if palabra[0] == ci:
                    no_encontrado=False
                    print("Estudiante de cedula ",ci," encontrado")
                    print("Primer parcial: ",palabra[4])
                    print("Segundo parcial: ",palabra[5])
                    print("Tercer parcial: ",palabra[6])
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
            p=linea.strip().split(',')
            if p[0] == ci:
                no_encontrado=False
                print("Esta seguro de eliminar al estudiante S/N")
                res=input()
                if res.upper()=='N':
                    print("Eliminacion cancelada")
                    file.write(linea)
                else:
                    print("Registro eliminado")
            else:
                file.write(linea)
                no_encontrado = True
        if no_encontrado:
            print("Estudiante no encontrado")
                    
def mostrar_aprobados():
    try:
        with open(archivo,'r') as file:
            no_en=True
            contenido = file.readlines()
            print(" ************APROBADOS***********")
            for linea in contenido:
                palabras = linea.strip().split(",")
                try:
                    num1 = float(palabras[6]) 
                    num2 = float(palabras[4])
                    num3 = float(palabras[5])
                    prom = (num1 + num2 + num3) / 3
                    if prom > 50.0:
                        no_en = False
                        print(linea, end="")
                except ValueError:
                        print(f"Error de conversión en la línea: {linea}")
            if no_en:
                print("No hay alumnos aprobados")
    except Exception as e:
        print(f"Se ha producido un error: {e}")
def mostrar_ordenados():
    ordenado=[]
    with open(archivo,'r') as file:
        lineas=file.readlines()
        for linea in lineas:
            datos=linea.strip().split(',')
            ordenado.append(datos)
    ordenado.sort(key=lambda x:x[1])
    with open(archivo, 'w') as file:
        for linea in ordenado:
            file.write(','.join(linea) + '\n')
    with open(archivo,'r') as file:
        lineas=file.readlines()
        for linea in lineas:
            print(linea, end="")
    
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
        ci=input("Ingrese la cedula: ")
        consultar_calificaciones(ci)

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
        ci=input("Ingrece la cedula del estudiante a eliminar: ")
        eliminar_registro(ci)
    if opc == 5:
        mostrar_aprobados()
    if opc == 6:
        mostrar_ordenados()
    if opc == 7:
        break


