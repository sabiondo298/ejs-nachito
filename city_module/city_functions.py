def ciudad_pais():
    ciudad = input("Ingrese el nombre de una ciudad: ")
    pais = input("Ingrese el nombre de un país: ")
    nombre = f"{ciudad.title()}, {pais.title()}"
    print(nombre)
    return nombre

ciudad_pais()