'''
Implemente el siguiente programa Orientado a objetos:
Celular
-marca: String
-modelo:String
-precio:double
+registrar()
+mostrar()
'''
class Celular:
    def __init__(self,marca="",modelo="",precio=0.0):
        self.marca=marca
        self.modelo=modelo
        self.precio=precio
    def __str__(self) -> str:
        return f"MARCA: {self.marca}    MODELO: {self.modelo}   PRECIO: {self.precio}"
    def registrar(self):
        self.marca=input("Ingrese la marca: ")
        self.modelo=input("Ingrese el modelo: ")
        self.precio=float(input("Ingrese el precio: "))
        print("Registro exitoso")
        
    def mostrar(self):
        print("Datos registrados")
        print(self)

cel=Celular()
cel.registrar()
cel.mostrar()