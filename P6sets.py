"""
 Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""

print("\033c")
set1={"Hola","123","123","Mexico","Holanda",123, 3.1416}
print(set1)
set1.add("Ganador")
print(set1)
set1.pop()
print(set1)

#ejemplo Crear un programa que solicite los email de los alumnos de la UTD almacenar en una lista y posteriormente mostrar en pantalla los email sin duplicados

#Solucion 1
emails = []

cantidad = int(input("\n¿Cuántos correos ingresaras?: "))

for i in range(cantidad):
    correo = input(f"Correo {i+1}: ")
    emails.append(correo)

print("\nLista original:")
print(emails)

emails_sin_duplicados = set(emails)

print("\nCorreos sin duplicados:")
print(emails_sin_duplicados)


#Solucion 2
correos = set()

cantidad = int(input("\n¿Cuántos correos ingresaras?: "))

for i in range(cantidad):
    correo = input(f"Correo {i+1}: ")
    correos.add(correo)



print("\nCorreos registrados sin duplicar:")
for correo in correos:
    print(correo)
