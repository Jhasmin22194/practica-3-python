'''
Define una clase "Animal" con atributos de nombre y edad. Implementa un método 
para imprimir la información del animal en pantalla
'''
class Animal():
    def __init__(self,nombre="",edad="") -> None:
        self.nom=nombre
        self.e=edad
    def __str__(self) -> str:
        return f"NOMBRE: {self.nom}     EDAD: {self.e}"
    
obj=Animal(input("Ingrese el nombre del animal: "), input("Ingrese la edad del animal: "))
print(obj)