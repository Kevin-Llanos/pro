for i in [1,2,3]:
	print("hola")

for i in ["primavera", "verano","otoño", "invierno"]:
	print(i)

#ahora veremos la función end al final de una función que se utiliza para escoger como quieres terminar cada función, ejemplo:

for i in [1, 2, 3]:
	print("Hola", end=", ")
print(" ")

#si solo despues del for utilizamos un string entonces ejecutará el bucle con cada elemento del string, ejemplo

for i in "cagada":
	print("c", end=", ")
print("")

#ahora tenemos los tipo range, es como crear una lista desde el 0 hasta la cantidad de números que fijemos, ejemplo:

for i in range(5):
	print(i, end=", ")
print("")
#también podemos agregar otro elemento para señalar hasta donde quiere que llegue el for y el primer elemento será desde cual empieza [).
for i in range(5,10):
	print(i, end=", ")
print("")
#y por último, si agregamos un elemento más indicaría como se contaría los números.
for i in range(5,50,3):
	print(i, end=", ")

#ahora intentaré hacer el verificador de correo electronico
ar=0
pn=False
email=input("ingrese el correo electronico")

for i in range(len(email)):
	if email[i]=="@":
		ar=ar + 1
	if email[i]==".":
		pn=True
if ar==1 and pn==True:
	print("email correcto")
else:
	print("correo incorrecto")

# como dato adicional el "else:" en los bucles for se da justo al final de un bucle