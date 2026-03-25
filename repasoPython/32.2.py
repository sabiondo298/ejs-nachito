with open("learning_python.txt", "r") as archivo:
    contenido = archivo.read()
    print("Leyendo todo el archivo")
    print(contenido)

with open("learning_python.txt", "r") as archivo:
    lineas = archivo.readlines()

print("Leyendo línea por línea")
for linea in lineas:
    print(linea)
