print("\033c")

#Ejemplo 1 Crear una lista de numeros e imprimir el contenido
numeros=[23,33,45,8,24,0,100]
lista=""
palabras=["UTD", "tercer", "cuatrimestre", "TI"]


print(numeros)
for i in range (0,len(numeros)):
    #lista=lista+str(i)+", "
    lista+=f"{numeros[i]}, "
print(f"[{lista}]")


i=0
while i<len(numeros):
    #lista=lista+str(i)+", "
    lista+=f"{numeros[i]}, "
    i+=1
print(f"[{lista}]")


#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra 
#1ERA FORMA

palabra=input("Dame la palabra a buscar: ")
if palabra in palabras:
    print(f"La palabra encontrada es: {palabra}")
else:
    print(f"No encontré la palabra: {palabra}")


#2DA FORMA
palabra=input("Dame la palabra a buscar: ")

encontro=False
for i in palabras:
    if i==palabra:
        encontro=True

if encontro:
    print(f"La palabra encontrada es: {palabra}")
else:
    print(f"No encontré la palabra: {palabra}")

#3er FORMA LEN

resp="si"

while resp.lower()=="si":
    nuevo=input("Dame una palabra para agregar: ")
    palabras.append(nuevo)

    resp=input("¿Deseas agregar otra palabra? ")

print("Contenido de la lista:")
for i in palabras:
    print(i)

#Ejemplo 3 Añadir elementos a la lista

lista=[]

bandera="True"
while bandera=="True":
    valor=input("Dame un valor: ").strip()
    lista.append(valor)
    bandera=input("Ingresa true or false para continuar: ").strip()

print(lista)
#opcion 2
bandera=True
while bandera==True:
    valor=input("Dame un valor: ").strip()
    lista.append(valor)
    bandera=input("Ingresa true or false para continuar: ").strip().lower()

    if bandera=="false".lower().strip():
        bandera=False
print(lista)



#Ejemplo 4 Crear una lista multidimensional que permita almacenar el nombre y telefono de una agenda
#while

agenda = [
    ["Carlos", "6183622485"],
    ["Adrian", "6183622484"],
    ["Luis", "6183622183"],
    ["Emely", "6185332535"]
]

for r in range(0, 3):
    for c in range(0, 2):
        print(agenda[r][c])

lista = ""
for r in range(0, 3):
    for c in range(0, 2):
        lista += f"{agenda[r][c]},"
    lista += "\n"

print(f"[{lista}]")