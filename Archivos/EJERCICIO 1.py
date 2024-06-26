'''
Escribir un programa para gestionar contactos telefónicos (contactos.txt) con los
nombres y los teléfonos de los clientes de una empresa. En el programa incorporar
funciones para:
• Crear el fichero si no existe
• Consultar el teléfono de un cliente
• Añadir el teléfono de un nuevo cliente
• Eliminar el teléfono de un cliente
• El fichero de texto contactos.txt debe contener el nombre del cliente y su teléfono
separados por comas y cada cliente debe estar en una línea distinta.
Juan Pérez,72598786
María Mamani,72595869
Luis Ticona,71595589
'''
import os
archivo = 'contactos.txt'

def crear_archivo():
    if not os.path.exists(archivo):
        with open(archivo, 'w') as file:
            pass
        print("Archivo de contactos creado.")
    else:
        print("El archivo de contactos ya existe.")

def consultar_telefono(nombre):
    try:
        no_encontrado=True
        with open(archivo, 'r') as file:
            for linea in file:
                cliente = linea.strip().split(',')
                if cliente[0].lower() == nombre.lower():
                    no_encontrado=False
                    if len(cliente) == 1:
                        print("El cliente no tiene telefono")
                    else:
                        print("Telefono: ",cliente[1])
        if no_encontrado:
            print("Cliente no encontrado")
    except FileNotFoundError:
        return "El archivo de contactos no existe."

def añadir_cliente(nombre, telefono):
    with open(archivo, 'a') as file:
        file.write(f"{nombre},{telefono}\n")
    print(f"Cliente {nombre} añadido con éxito.")

def eliminar_telefono(nombre):
    try:
        with open(archivo, 'r') as file:
            lineas = file.readlines()
        
        with open(archivo, 'w') as file:
            no_encontrado = True
            for linea in lineas:
                cliente = linea.strip().split(',')
                if cliente[0].upper() != nombre.upper():
                    file.write(linea)
                else:
                    no_encontrado = False
                    print("Esta seguro de eliminar S/N")
                    res=input()
                    if res.upper() == 'S':
                        file.write(f"{cliente[0]}\n")     
                        print("Telefono eliminado correctamente")            
        if no_encontrado:
            print("Cliente no encontrado")
    except FileNotFoundError:
        print("El archivo de contactos no existe.")
        
def mostrar_contactos():
    with open(archivo, mode='r') as file:
        datos = file.readlines() 
        print("*"*30)
        for i in datos:
            print(i, end="")
        print("*"*30)
        
def menu():
    print("Elige una opcion")
    print("1. Consultar el teléfono de un cliente")
    print("2. Añadir el teléfono de un nuevo cliente")
    print("3. Eliminar el teléfono de un cliente")
    print("4. Mostrar todos los contactos")
    print("5. Salir")
    opc=int(input())
    return opc

# Crear el archivo
crear_archivo()
while (True):
    opc=menu()
    if opc == 1:
        print("Ingrese el nombre del cliente ")
        nombre=input()
        consultar_telefono(nombre)
    if opc == 2:
        nom=input("Nombre: ")
        num=input("Telefono: ")
        añadir_cliente(nom,num)

    if opc == 3:
        nom=input("Ingrese el nombre del cliente ")
        eliminar_telefono(nom)
    if opc == 4:
        mostrar_contactos()
    if opc == 5:
        break


