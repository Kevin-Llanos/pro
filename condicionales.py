# condicional if
print ("holiwis")
nota_=int(input())
def evaluacion (nota):
	valor="aprobado"
	if nota<3:
		valor="reprobado"
	return valor

print (evaluacion(nota_))

#ejemplo con el else para negar un if (como ya sabe como hacer desde racket)

print ("verificación de adulterio xd")

edad=int(input("poné tu edad horrorosa aquí o verás"))

if edad>=18:
	if edad>99:
		print("no puede ejecutar esa acción, imbecil de mierda")
	else: print("eres mayor en colombia")
else: 
	if edad<12:
		print("buena aguevado")
	else: print("aguevado de mierda")


#se puede hacer de manera mas corta y utilizando el elif que funciona como un else if

if edad<18:
	print("no llega")
elif edad>99:
	print("se pasa de imbecil")
else:
	print("ya pase bobo mk")