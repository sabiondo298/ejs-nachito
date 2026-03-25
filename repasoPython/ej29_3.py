class privilegios:
    def __init__(self):
        self.privilegios = ["puede agregar publicaciones", "puede eliminar publicaciones", "puede banear usuarios"]

    def mostrar_privilegios(self):
                print("Privilegios del administrador:")
                for privilegio in self.privilegios:
                    print(f"- {privilegio}")

class admin:
        def __init__(self, nombre, apellido, edad):
            self.nombre = nombre
            self.apellido = apellido
            self.edad = edad
            self.privilegios = privilegios()

if __name__ == "__main__":
    admin1 = admin("juan", "giuri", 16)
    admin1.privilegios.mostrar_privilegios()