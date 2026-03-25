lista = ["juan", "pedro", "maria", "lucia", "admin"]
for i in lista:
    if i == "admin":
        print("Hola admin, ¿deseas ver un reporte de usuarios?")
    else:
        print(f"Hola {i}, gracias por iniciar sesión.")