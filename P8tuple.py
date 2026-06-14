"""   

  Las tuplas se utilizan para almacenar varios elementos en una sola variable.

   Una tupla es una colección ordenada e inmutable .

   Las tuplas se escriben entre paréntesis.


"""
print("\033c")

paises=("Mexico","Canada","EUA")
paises3=["Mexico","Canada","EUA"]
varios=("Hola",True,33,3.14)


paises3[1]="Brasil"


print(paises)
print(varios)
print(paises3)

for i in paises:
    print(i)

for i in range(0,len(paises)):
    print(paises[i])
    
print(f"El pais que inagura la copa del mundo 2026 es: {paises[0]}")

i=0
while i<3:
    print(paises[i])
    i+=1

edades=(23,24,18,20,20,23,24,19,24)

cuantos=edades.count(24)
print(f"El numero 24 se repite {cuantos} veces")



#Crear un programa que me lea un numero y me diga en que posiciones se encuentra con .index()
edades=(23,24,18,20,20,23,24,19,24)
num=int(input("Ingrese un numero del 18 al 24: "))
posicion=edades.index(num)
print(f"El numero {num} se encuentra en la posicion: {posicion}")

numero=int(input("Ingrese un numero del 18 al 24: "))
posiciones={""}
posiciones.clear()  
for i in range(len(edades)):
    if edades[i]==numero:
        posiciones.append(i)
posiciones=tuple(posiciones)

for i in posiciones:
    print(f"El numero {numero} se encuentra en la posicion: {i}")





#Utilizando tuplas
numero=int(input("Ingrese un numero del 18 al 24: "))
posiciones={""}
posiciones.clear()  
for i in range(len(edades)):
    if edades[i]==numero:
        posiciones.append(i)
posiciones=tuple(posiciones)

for i in posiciones:
    print(f"El numero {numero} se encuentra en la posicion: {i}")

#Utilizando set
numero=int(input("Ingrese un numero del 18 al 24: "))
posiciones=set()
for i in range(len(edades)):
    if edades[i]==numero:
        posiciones.add(i)
for i in posiciones:
    print(f"El numero {numero} se encuentra en la posicion: {i}")   
    
    
    







