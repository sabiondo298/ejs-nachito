class restaurante:
    def __init__(self, nombre, tipo_cocina, clientes_atendidos=0):
        self.nombre = nombre
        self.tipo_cocina = tipo_cocina
        self.clientes_atendidos = clientes_atendidos

    def describir_restaurante(self):
        print(f"El restaurante {self.nombre} ofrece comida {self.tipo_cocina}.")

    def abrir_restaurante(self):
        print(f"El restaurante {self.nombre} está abierto.")

    def establecer_clientes_atendidos(self, numero):
        self.clientes_atendidos = numero    
        print(f"El número de clientes atendidos se ha establecido en {self.clientes_atendidos}.")

mi_restaurante = restaurante("Luigi, il conto, per favore.", "italiana")
mi_restaurante.describir_restaurante()
mi_restaurante.abrir_restaurante()
mi_restaurante.establecer_clientes_atendidos(10)