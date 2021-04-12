class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludo(self):
        print ("Hola, mi nombre es", self.nombre, self.apellido)

usuario = Usuario("Kevin", "Llanos")
usuario2 = Usuario("Chanchito", "Feliz")

usuario.saludo()
usuario2.saludo()

print (usuario.nombre, usuario.apellido, usuario2.nombre, usuario2.apellido)

class Admin(Usuario):
    def supersaludo(self):
        print ("Hola, me llamo", self.nombre, "Y soy admin")

admin = Admin("Super", "Feliz")
admin.saludo()   #acá podemos observar como la clase hija (admin) puede utilizar lo que ya se tenía en la clase padre (Usuario)
admin.supersaludo() #y aquí vemos como utiliza algo exclusivo de su clase
usuario.supersaludo() #aquí veremos que la clase padre no puede utilizar ningún metodo de la clase hija