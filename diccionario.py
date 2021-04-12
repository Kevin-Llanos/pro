#vamos con los diccionarios que se crean con llaves {} y su sintaxis es una clave, dos puntos y acontinuación el valor
diccionario={"Colombia":"Bogotá", "Alemania":"Berlin", "USA":"Washington"}
#clave-valor, al poner la clave (en este ejemplo el país) y nos da el valor (en este caso es la capital)
print (diccionario ["Colombia"])
#agregar un nuevo elemento al diccionario
diccionario["Risaralda"]="Pereira"
print (diccionario)
#para reemplazar un valor de una clave se escribe como si se fuera a agregar una nueva
diccionario["Alemania"]="mitocondria"
print (diccionario)
#y para eliminar un elemento se utiliza el "DEL" o el método .pop("")
del diccionario["Alemania"]
print (diccionario)
diccionario.pop("USA")
print (diccionario)
#también se puede eliminar el último elemento del diccionario utilizando el método .popitem
diccionario.popitem()
#si queremos ver las claves podemos usar
print (diccionario.keys())
print (diccionario.values())
print (len(diccionario))

#también podemos copiar un diccionario con el método .copy()
print ("copia hecha:")
copiaDic = diccionario.copy()
print (copiaDic)
#Y también limpiar todo un diccionario con el método .clear()
print ("copia borrada:")
copiaDic.clear()
print (copiaDic)