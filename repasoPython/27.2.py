class restaurante:
    def __init__(self, nombre, tipo_cocina):
        self.nombre = nombre
        self.tipo_cocina = tipo_cocina

    def describir_restaurante(self):
        print(f"El restaurante {self.nombre} ofrece comida {self.tipo_cocina}.")

    def abrir_restaurante(self):
        print(f"El restaurante {self.nombre} está abierto.")

mi_restaurante1 = restaurante("Luigi, il conto, per favore.", "italiana")
mi_restaurante1.describir_restaurante()
mi_restaurante1.abrir_restaurante()

mi_restaurante2 = restaurante("las cabras chicken", "estadunidense")
mi_restaurante2.describir_restaurante()
mi_restaurante2.abrir_restaurante()

mi_restaurante3 = restaurante("marde de ajo sin hoes", "española")
mi_restaurante3.describir_restaurante()
mi_restaurante3.abrir_restaurante()