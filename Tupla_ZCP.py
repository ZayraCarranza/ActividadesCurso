##Actividad : Tupla
##1.- Crea una tupla con una longitud de 5 usando diferentes tipos de datos.
##2.- Cambiar dicha tupla a una lista.
##3.- Crea un diccionario donde la clave sea del 1 al 5 y los elementos los datos de la lista.
##Utilizar la función "list" para la elaboración de la actividad.


print("Actividad 2 Tupla. Zayra Carranza Portillo")


tupla = ("Jupiter", None, "Zapato", 3.1416)

print("Convierte a tupla:")
tupla1 = tuple(tupla)
print(tupla)

print ("Convertir la tupla a lista")
#Utilizando la función List 
t_1 = list(tupla)
print(t_1)

##Diccionario
print("Crea un diccionario")

diccionario = {"Jupiter" :1 ,
                None : 2,
                "Zapato" : 3,
                3.1416 : 4 ,
                "Caballeros": 5,}

print(diccionario)

print(diccionario['Jupiter'])
print (diccionario['Zapato'])
print (diccionario['Caballeros'])

