class restaurante:
    def __init__(self, nombre, tipo_cocina):
        self.nombre = nombre
        self.tipo_cocina = tipo_cocina

    def describir_restaurante(self):
        print(f"El restaurante {self.nombre} ofrece comida {self.tipo_cocina}.")

    def abrir_restaurante(self):
        print(f"El restaurante {self.nombre} está abierto.")

if __name__ == "__main__":
    mi_restaurante = restaurante("Luigi, il conto, per favore.", "italiana")
    mi_restaurante.describir_restaurante()
    mi_restaurante.abrir_restaurante()