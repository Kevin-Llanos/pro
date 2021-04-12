#ahora vamos a crear un diccionario dentro de otro diccionario:

gatitos = {
    "Fluffy": {
        "nombre": "Fluffy",
        "edad": 4
    },
    "Mamba": {
        "nombre": "Mamba",
        "edad": 4
    }
}

print (gatitos)
print (gatitos.keys())

#podemos crear diccionarios de otra forma:
perritos = dict(nombre="Kiba", edad=5)
print (perritos)
