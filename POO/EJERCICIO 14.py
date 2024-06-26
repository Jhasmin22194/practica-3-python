'''
Crea una clase "Tienda" con atributos de nombre y lista de productos. Implementa un 
método para agregar un nuevo producto a la tienda.
'''
class Tienda:
    def __init__(self,nombre="",lista_productos=[]) -> None:
        self.nombre=nombre
        self.lista_productos=lista_productos
    def mostrar(self):
        print("_"*50)
        print(f"NOMBRE: {self.nombre}")
        print("_____________LISTA DE PRODUCTOS____________")
        for i in self.lista_productos:
            print(i)
    
    def agregar_p(self):
        n=int(input("Ingrese la cantidad de productos a ingresar: "))
        for _ in range(n):
            self.lista_productos.append(input("Producto: "))
        print("Lista de productos añadido")

obj=Tienda(input("Ingrese el nombre de la tienda: "),[input("Producto: ")])
obj.mostrar()
obj.agregar_p()
obj.mostrar()