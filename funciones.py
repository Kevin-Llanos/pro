# Existe un simbolo reservado para que en un argumento se puedan recibir varios, este es el "*"

def a(*b):
	print (b)

a("a", "b", "c") #pero los almacena como una lista

#podemos utilizar el nombre de los argumentos de una función para darle su valor

def nomBre (nombre, apellido):
	print (nombre, apellido)

nomBre(nombre="Kevin", apellido="Llanos")

#ahora vamos a ver como utilizar una función con sus argumentos como un diccionario (KWARGS)

def Nombre (**kwargs):
	print(kwargs["nombre"], kwargs["apellido"])

Nombre (nombre="Kevin", apellido="Llanos")