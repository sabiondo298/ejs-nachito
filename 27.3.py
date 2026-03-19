class usuario:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

        def describir_usuario(self):
            print(f"El usuario se llama {self.nombre} {self.apellido} y tiene {self.edad} años.")

        def saludar_usuario(self):
            print(f"Hola {self.nombre}, ¡bienvenido de nuevo!")

        usuario1 = usuario("Nacho", "Gonzalez", 20)
        usuario1.describir_usuario()
        usuario1.saludar_usuario()

        usuario2 = usuario("María", "Gómez", 25)
        usuario2.describir_usuario()
        usuario2.saludar_usuario()
        
        