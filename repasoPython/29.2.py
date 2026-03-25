class admin:
        def __init__(self, nombre, apellido, edad, privilegios):
            self.nombre = nombre
            self.apellido = apellido
            self.edad = edad
            self.privilegios = privilegios = ["puede agregar publicaciones", "puede eliminar publicaciones", "puede banear usuarios"]

        def mostrar_privilegios(self):
                print("Privilegios del administrador:")
                for privilegio in self.privilegios:
                    print(f"- {privilegio}")
        
admin1 = admin("juan", "perez", 30, ["puede agregar publicaciones", "puede eliminar publicaciones", "puede banear usuarios"])
admin1.mostrar_privilegios()
        