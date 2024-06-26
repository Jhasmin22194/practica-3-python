'''
Implemente la siguiente clase empleando la Programación Orientada a Objetos.
Computadora
- hdd: entero
-marca: cadena
-precio: real
+ registrar()
+ mostrar()
+ actualizar()
'''
class Computadora:
    def __init__(self, hdd=0, marca="", precio=0.0):
        self.hdd = hdd
        self.marca = marca
        self.precio = precio
    
    def __str__(self):
        return f"HDD: {self.hdd}   MARCA: {self.marca}   PRECIO: {self.precio}"
    
    def registrar(self):
        self.hdd = int(input("Ingrese el tamaño del HDD en GB: "))
        self.marca = input("Ingrese la marca de la computadora: ")
        self.precio = float(input("Ingrese el precio de la computadora: "))
        print("Registro exitoso")
    
    def actualizar(self):
        while True:
            print("1. Modificar HDD")
            print("2. Modificar Marca")
            print("3. Modificar Precio")
            print("4. Salir")
            opc=int(input())
            match opc:
                case 1:
                    self.hdd=int(input("HDD: "))
                case 2:
                    self.marca=input("Marca: ")
                case 3:
                    self.precio=float(input("Precio: "))
                case _:
                    print("Hasta luego!!!...............")
                    break
    
    def mostrar(self):
        print(self)

# Ejemplo de uso de la clase Computadora
comp = Computadora()
comp.registrar()
print("\nInformación de la computadora registrada:")
comp.mostrar()
print("\nActualización de la computadora:")
comp.actualizar()
print("\nInformación actualizada de la computadora:")
comp.mostrar()
