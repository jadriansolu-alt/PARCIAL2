# 1er utilizar los modulos 
import modulos 
nom="daniel"
ape="carreon"
modulos.borrarPantalla()
#llamar funcion1
modulos.funcion1()
#llamar funcion3
modulos.funcion3(nom,ape)
#llamar funcion4
nombre,apellidos=modulos.funcion4(nom,ape)
print(f"Nombre:{nombre} \n Apellidos: {apellidos}")
#2da formar de utilizar modulos
from modulos import borrarPantalla, funcion4
borrarPantalla()
nom="daniel"
ape="carreon"
nombre,apellido=funcion4(nom,ape)
print(f"nombre: {nombre}\ apellido: {apellido}")
