# hemos creado una especie de matriz donde podemos ver que los elementos en la primera dimension son las palabras pero a su vez tiene sub elementos como lo son las letras
def devuelve_ciudades(*ciudades):
	for elemento in ciudades:
		yield elemento

ciudades_devueltas=devuelve_ciudades("pereira", "dosquebradas", "zarzal")

print(next(ciudades_devueltas))

# para poder ver cada una de las letras de los elementos debemos anidar dos for:

def devuelve_ciudades(*ciudades):
	for elemento in ciudades:
		for subelemento in elemento:
			yield subelemento

ciudades_devueltas=devuelve_ciudades("pereira", "dosquebradas", "zarzal")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))

# PD: se puede simplificar esa sintaxis usando una opción de python la cual es "yield from"

def devuelve_ciudades(*ciudades):
	for elemento in ciudades:
		#for subelemento in elemento:
			yield from elemento

ciudades_devueltas=devuelve_ciudades("pereira", "dosquebradas", "zarzal")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))