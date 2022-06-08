class Docente:
    def __init__ (self,nombre,apellido,edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
    
def historialDoc():
    print("Los docentes que se registraron son los siguientes")
    print(nombre)
    print(apellido)
    print(edad)
    

numDoce=int(input("Ingrese cuantos docentes se van a registrar :"))
for i in range (numDoce):
    nombre=input("Ingrese su nombre: ")
    apellido=input("Ingrese su apellido: ")
    edad=input("Ingrese sus anios de edad: ")

d=Docente

for i in range (0,numDoce):
    print("El nombre es: ",nombre)
    print("El apellido es: ",apellido)
    print("El edad es: ",edad)