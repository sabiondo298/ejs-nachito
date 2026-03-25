class usuario:
    def __init__(self, nombre, apellido, edad, intentos_login=0):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.intentos_login = intentos_login

    def describir_usuario(self):
            print(f"El usuario se llama {self.nombre} {self.apellido} y tiene {self.edad} años.")

    def saludar_usuario(self):
            print(f"Hola {self.nombre}, ¡bienvenido de nuevo!")

    def incrementar_intentos_login(self):
            self.intentos_login += 1
            print(f"Intentos de login incrementados a {self.intentos_login}.")

    def resetear_intentos_login(self):
            self.intentos_login = 0
            print(f"Intentos de login reseteados a {self.intentos_login}.")

usuario1 = usuario("Nacho", "Gonzalez", 20)
usuario1.describir_usuario()
usuario1.saludar_usuario()
usuario1.incrementar_intentos_login()
usuario1.resetear_intentos_login()

usuario2 = usuario("María", "Gómez", 25)
usuario2.describir_usuario()
usuario2.saludar_usuario()
usuario2.incrementar_intentos_login()
usuario2.resetear_intentos_login()