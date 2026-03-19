respuesta = input("¿Cuál es tu edad? (escriba 0 para terminar): ")
while respuesta != "0":
    edad = int(respuesta)
    if edad < 3:
        print("La entrada es gratuita")
    elif 3 <= edad < 12:
        print("El precio de la entrada es $10")
    else:
        print("El precio de la entrada es $15")
    respuesta = input("¿Cuál es tu edad? (escriba 0 para terminar): ")