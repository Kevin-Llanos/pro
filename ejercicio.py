a=int(input("ingrese el primer número"))
b=int(input("ingrese el segundo número"))

if a==b:
	print ("ambos números son iguales")
elif a>b:
	print ("el primer número que ingresó es mayor que el segundo")
else:
	print ("el segundo número es mayor al primero que ingresó")



# media aritmetica

a=int(input("ingrese el primer numero"))
b=int(input("ingrese el segundo numero"))
c=int(input("ingrese el terecer numero"))

def media(a, b, c):
	M=(a+b+c)//3
	return M

print (media(a, b, c))