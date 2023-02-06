##Actividad: Operaciones Edad - Ecuaciones
##1.-El doble de mi edad tiene 24 años, ¿cuántos años tengo? (x=?)
##2.- A un tercio de la edad de mi hermana le disminuyo 15 años para tener la misma edad que yo. Yo tengo 6 años. ¿Qué edad tiene ella? (Escribir la ecuación correspondiente, despejar y calcular la nueva variable "y" de manera manual)
##3.-Determina quién es más grande (variables "x" y "y") utilizando if y else.

print("Actividad 5 Ecuaciones. Zayra Carranza Portillo")

## 1. El doble de mi edad

DobleEdad = 24
X = 24 / 2 
Edad = X
print("Mi edad es:" , Edad)

## 2. ¿Qué edad tiene ella?
print ("2. A un tercio de la edad de mi hermana le disminuyo 15 años para tener la misma edad que yo. Yo tengo 6 años. ¿Qué edad tiene ella? : ")
print("( y / 3 ) -15 = 6")
print("Despejando 'y' ")
print("y = (6 + 15)*3")
y = (6+15)*3
print("Su edad es: ", y)

##3. Determina quién es más grande
print("3. Determina quién es más grande")
if X > y :
    print("Mi edad es mayor ya que es: ", X)
else :
    print("Mi hermana es mayor ya que su edad es: ", y)


    