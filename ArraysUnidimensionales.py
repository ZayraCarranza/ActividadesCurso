##Actividad: Arrays Unidimensionales
##1.- Crea un vector utilizando la función np.array() con valores dentro del rango 3 al número que representa tu edad. Por ejemplo, 
# #si usted tiene 30 años, el vector debería de contener los números 3, 4, 5, ... , 30.
##2.- Crea un arreglo con los siguientes elementos: [0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
##3.- Ordena de forma ascendente dicho arreglo utilizando la función .sort().

print("Arrays Unidimensionales.     Zayra Carranza Portillo")


import numpy
import numpy as np


print("Vector con función np.array()")
vector = np.array([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26])
print(vector)

#Usando range
#vector1 = np.array([i for i in range(27)])
#print(vector1)

#otra opción
a = numpy.arange(start = 3 , stop= 27, step=1)
print(a)

print("Crea un arreglo con los siguientes elementos: ")
#2. Crea un arreglo con los siguientes elementos
arreglo = np.array([0,1,2,3,4,0,1,2,3,4])
print(arreglo)

#3. Ordena de forma ascendente
print("3. Ordena de forma ascendente")
ordena = sorted(arreglo)
print(ordena)