class puesto_de_helados:
    def __init__(self, nombre, sabores):
        self.nombre = nombre
        self.sabores = sabores

    def describir_puesto(self):
        print(f"El puesto de helados {self.nombre} ofrece los siguientes sabores:")
        for sabor in self.sabores:
            print(f"- {sabor}")

mi_puesto_de_helados = puesto_de_helados("Heladerio boludin", ["chocolate", "vainilla", "fresa", "menta"])
mi_puesto_de_helados.describir_puesto()
