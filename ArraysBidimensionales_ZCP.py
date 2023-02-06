#Actividad: Arrays Bidimensionales
#1.- Crear una matriz 3x3 con valores de 0 a 8
#2.- Crear una matriz identidad de 6x6 utilizando la función .identity().

print("Arrays Bidimensionales.     Zayra Carranza Portillo")

import numpy
import numpy as np

print("1. Crear una matriz 3x3 con valores de 0 a 8: ")

matriz = np.array([[0,1,2],[3,4,5],[6,7,8]])
print(matriz)

##Otra opción
print ("otra opción: ")
a = np.arange(0, 9).reshape(3, 3) 
print(a)

print("2. Crear una matriz identidad de 6*6 con función .identity() ")

MIdentidad = np.identity(6)
print(MIdentidad)