#el bucle while
i=1

while i<10:
	print("ejecución", i)
	i=i+1

#se puede utilizar de la siguiente manera con el ejemplo de la edad correcta e incorrecta:
edad=int(input("ingrese su edad "))

while edad<=0 or edad>100:
	print("su edad es incorrecta, intente nuevamente ")
	edad=int(input("ingrese su edad "))
print ("su edad,", edad, "años, es correcta")

#vamos a hallar la raiz cuadrada de un número dado por el usuario
import math
intentos=3
intento=0
numero=int(input("ingrese un número acontinuación (tienes " + str(intentos) + " oportunidades): "))

while numero < 0:
	print("no se puede hallar una raiz negativa")

	if intento==2:
		print("cagada mija")
		break;

	if numero<0:
		intento=intento+1
		intentos=intentos-1

	numero=int(input("ingrese un número acontinuación (tienes " + str(intentos) + " oportunidades): "))

if intento<2:
	print("la raiz cuadrada de", numero , "es igual a", math.sqrt(numero))

#Ahora tenemos la función "continue;" esta se utiliza para que el bucle se salte el resto de instrucciónes e inicie un nuevo giro

i = 0

while i < 5:
	i = (i + 1)
	if i == 2:
		continue;
	print(i)