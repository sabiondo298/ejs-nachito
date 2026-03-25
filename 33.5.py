try:
    with open('gatos.txt', 'r') as f:
        print("Contenido de gatos.txt:")
        print(f.read())
    with open('perros.txt', 'r') as f:
        print("Contenido de perros.txt:")
        print(f.read())
except FileNotFoundError:
    print("Lo siento, uno de los archivos no se encuentra, verifica que ambos archivos estén en la carpeta.")
