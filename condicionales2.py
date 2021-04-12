#ejemplo de como se podría utilizar un if mas facil para varias condiciones

edad=int(input("ingrese la edad"))

if 0<=edad<=100:
	print("edad incorrecta")
else:
	print ("edad es correcta, garcias")

#ahora vamos a probar con los "and" y "or"
#lo haré con un ejemplo sobre una beca

distancia=int(input("ingrese la distancia"))
hermanos=int(input("ingrese el número de hermanos"))
salario=int(input("ingrese el salario de su familia"))

if distancia>40 and hermanos>4 or salario<20000:
	print("tienes derecho a beca")
else:
	print("no tienes ni verga")

#condicional in para buscar dentro de una lista

print ("asignaturas: math, español, fisica")
asig=input("ingrese la asignatura que escogerá")
asignatura=asig.lower()

if asignatura in ("math", "español", "fisica"):
	print("asignatura escogida:" + asignatura)
else: 
	print("eso no es ninguna asignatura nombrada, petardo")

#aquí solo voy a crear una pequeña aplicación 
dato = input("ingrese dato: ")

lista = ["Hola", "mundo", "me", "llamo", "kevin"]

if lista.count(dato) > 0: #aquí contamos cuantas veces se encuentra el dato dentro de la lista, solo necesitamos saber que esté dentro
	print ("el dato existe dentro de la lista")
else: 
	print ("el dato no existe, sorry mazamorry")

#ahora voy a crear una pequeña calculadora

primero = input("ingrese un valor: ")

# Con la instrucción "try" lo que hace es intentar realizar una función, si por alguna excepcíon la función no se realiza entonces hará otra cosa

try:
	primero = int(primero)
except:
	primero = "X"

if primero == "X":
	print ("acabas de ingresar un valor erroneo")
	exit()

#aquí ingresaré la operación que quiera realizar el usuario
lista = ["+", "-", "*", "/"]
operacion = str(input("ingrese la opreación que desea realizar (+, -, *, /)"))

segundo = input("ingrese el segundo valor: ")

try:
	segundo = int(segundo)
except:
	segundo = "X"

if segundo == "X":
	print ("acabas de ingresar un valor erroneo")
	exit()

def operar (primero, segundo, operacion):
	if operacion == "+":
		print (primero + segundo)
	elif operacion == "-":
		print (primero - segundo)
	elif operacion == "*":
		print (primero * segundo)
	elif operacion == "/":
		print (primero / segundo)
	else: print ("la operacion no coincide con ninguna de las dispuestas")

operar (primero, segundo, operacion)