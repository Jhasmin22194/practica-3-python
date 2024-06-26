'''
 Crea una clase "Libro" con atributos de título, autor y precio. Implementa un método 
para calcular el descuento del libro (por ejemplo, un 10% de descuento).
'''

class Libro:
    def __init__(self, titulo="",autor="", precio=0.0) -> None:
        self.titulo=titulo
        self.autor=autor
        self.precio=precio
    
    def __str__(self) -> str:
        return f"TITULO: {self.titulo}  AUTOR: {self.autor} PRECIO: {self.precio}"
    
    def descuento(self):
        des=int(input("Ingrese el descuento: "))
        print("Descuento del ",des,"% = ",self.precio-(self.precio*des/100) )
        
obj=Libro(input("Ingrese el nombre del libro: "),input("Ingrese el nombre del autor: "),float(input("Ingrese el precio del libro: ")))
print(obj)
obj.descuento()