with open("learning_python.txt", "r") as archivo:
    lineas = archivo.readlines()

print("Líneas originales:")
for linea in lineas:
    print(linea.strip())

print("\nLíneas modificadas (python reemplazado por C):")
for linea in lineas:
    linea_modificada = linea.replace("python", "C")
    print(linea_modificada.strip())