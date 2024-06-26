'''
Define una clase "Estudiante" con atributos de nombre, edad y promedio. Implementa
un método para determinar si el estudiante está aprobado o no (si su promedio es
mayor o igual a 6)
'''
class Esctudiante:
    def __init__(self, nombre="",edad=0,promedio=0.0):
        self.nombre=nombre
        self.edad=edad
        self.promedio=promedio
        
    def __str__(self):
        return f"NOMBRE: {self.nombre}  EDAD:{self.edad}    PROMEDIO: {self.promedio}"