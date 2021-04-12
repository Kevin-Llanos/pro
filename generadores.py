# los generadores ¿Qué son?
# empezaremos creando una función normal y corriente

def generaPares(limite):

	num=1

	lista=[]

	while num<limite:

		lista.append(num*2)

		num=num+1

	return lista

print(generaPares(10))

#ahora vamos a crear un generador

def GeneraPares(limite):

	num=1

	# hemos quitado la lista ya que el generador crea una lista interable por si mismo

	while num<limite:

		yield num*2 #esta es la función yield que se usa para los generadores

		num=num+1

#ahora debemos crear una variable donde vamos a guardar el objeto creado y donde vamos a recorrer el generador

devuelvePares=GeneraPares(10)

for i in devuelvePares:

	print (i)
