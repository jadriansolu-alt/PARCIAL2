"""  
 List (Array)
 son colleciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores se hace con un indice numerico 

 Nota: sus valores si son modificables

 La lista es una colección ordenada y modificable. Permite miembros duplicados.

"""
#Funciones más comunes en las listas

paises=["Mexico", "Canada", "EUA","Mexico", "Brasil"]
numeros=[23,45,8,24]
varios=[33,3.1416,"hola",True]
vacio=[]
#Imprimir el contenido de una lista
print(paises)
print(numeros)
print(varios)
print(vacio)
print(paises[0]+""+paises[3])
#Recorrer la lista 
#1er forma  
for i in paises: #guardas un dato
    print(i)
    print(i) #i trae el contador 
# #2do forma 
for i in range(0,5): #guardas un numero 
 print(paises[i])


print("\033c")
paises=["Mexico", "Canada", "EUA","Mexica", "Brasil"]
#ordenar elementos de una lista
paises.reverse()
print(paises)
print("\033c")
paises=["Mexico", "Canada", "EUA","Mexica", "Brasil"]
print(paises)
#Agregar, insertar, Añadir un elemento a una lista
#1er forma 
paises.append("honduras")
print(paises)
#2da forma
paises.insert(1,"argentina") 
print(paises)
#3 
paises.insert(100,"panama")
print(paises)
#Eliminar, borrar, suprimir, un elemento de una lista
#1er forma
paises.pop(4)
print(paises)
#2da forma 
paises.remove("EUA")
print(paises)
#Buscar un elemento dentro de la lista
buscar="Brasil" in paises
print(buscar)

#Contar el numeros de veces que aparece un elemento dentro de una lista solo de una lista numericos
numeros=[23,45,24,8,23,50,23]
cuantas=numeros.count(23)
print(f"el numero 23 aparece: {cuantas} veces ")

n=int(input("ingrese el numero que desea buscar"))
cuantas=numeros.count(n)
print(f"el numero {n} aparece: {cuantas} veces ")

posicion=numeros.index(50)
print(f"estoy en la posicion {posicion}")

numeros1=[23,45,24,8,23,50,23]
numeros2=[100,-100]
print(numeros2)
numeros1.extend(numeros2)
print(numeros1)

#Crear a partir de las listas de numeros 1 y 2 un resultante y mostar el contenid ordenado
# descendentemente
numeros1=[23,45,24,8,23,50,23]
numeros2=[100,-100]
print(numeros2)
numeros1.extend(numeros2)
print(numeros1)
numeros1.sort()
numeros1.reverse()
print(numeros1)

