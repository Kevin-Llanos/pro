#vamos a crear una clase de gato

class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya

    def saludo(self):
        print ("Hola, soy un", self.tipo, "me llamo", self.nombre, "y mi sonido es", self.onomatopeya)


class Gato(Animal):
    tipo = "gato"
    
gato = Gato("Fluffy", "maullido")
gato.saludo()

class Perro(Animal):   
    tipo = "perro"

perro = Perro("Kiba", "ladrido")
perro.saludo()

#con el canario y loro vamos a ver dos formas de como extender un método __init__

class Canario(Animal):
    tipo = "canario"
    def __init__(self, nombre, onomatopeya):
        Animal.__init__(self, nombre, onomatopeya)
        print ("Hola, soy un canario expandido")

canario = Canario("pepe", "silvido")
canario.saludo()

class Loro(Animal):
    tipo = "loro"
    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya)
        print ("Hola, soy un loro expandido")

loro = Loro("cacao", "imitar")
loro.saludo()    