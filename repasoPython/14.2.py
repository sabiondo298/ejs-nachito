lista = []
if lista == []:
    print("No hay usuarios registrados.")
    for i in lista:
        if i == "admin":
            print("Hola admin, ¿deseas ver un reporte de usuarios?")
            print("No hay usuarios registrados.")
        else:
            print(f"Hola {i}, gracias por iniciar sesión.")