#tenemos otras funciones para los condicionales como son continue, pass y else

#continue se utiliza para saltar una parte del codigo, por ejemplo

for letra in "python":

	if letra=="h":
		continue

	print ("viendo la letra: " + letra)

#en este ejemplo podemos ver como al encontrar la letra "h" el programa se salta la siguiente instrucción y continua con la siguiente vuelta del bucle

#otro ejemplo lo podemos hacer para contar las letras de una oracion, ya que si usamos el len() nos da la cantidad completa de caracteres que se encuentran

oracion="hola putos"
contador=0

for i in oracion:

	if i==" ":
		continue

	contador= contador + 1

print ("la cantidad de letras es " + str(contador))

#un break; lo que hace es parar el programa al llegar a un momento especifico
# adicionalmente encontramos el else a la altura de bucle

email=input("introduce email: ")

for i in email:

	if i=="@":

		arroba=True

		break;

else:

	arroba=False

print(arroba)