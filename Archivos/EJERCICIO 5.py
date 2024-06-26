'''
Escribir un programa que lea un archivo de texto con registros de personas y genere un
nuevo archivo de texto con los nombres y apellidos invertidos
'''

def invertir(archivo):
    with open(archivo,"r") as file:
        cont=file.readlines()
    with open("comz.txt","w") as file:
        for linea in cont:
            pal=linea[::-1].strip().split(",")  
            pal[0],pal[1]=pal[1],pal[0]   
            n_linea=",".join(pal)+"\n"
            file.write(n_linea)
                

def mostrar(archivo):
    with open(archivo,"r") as file:
        contenido=file.readlines()
        print("-"*40)
        for linea in contenido:
            print(linea.replace(",","\t"), end="")
        print("\n","-"*40)

while (True):
    print("\t MENU DE OPCIONES")
    print("1. Voltear un empleado")
    print("2. Mostrar empleados")
    print("3. Salir")
    opc=int(input())
    match opc:
        case 1:
            invertir("com.txt")
            mostrar("comz.txt")
        case 2:
            mostrar("com.txt")
        case _:
            print("Hasta luego!!!.................")
            break