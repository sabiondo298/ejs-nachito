usuarios_actuales = ["juan", "pedro", "maria", "lucia", "admin"]
usuarios_nuevos = ["ana", "carlos", "laura", "pedro", "juan"]
for usuario in usuarios_nuevos:
    if usuario in usuarios_actuales:
        print(f"El nombre de usuario '{usuario}' ya está en uso. Por favor, elige otro.")
    else:
        print(f"El nombre de usuario '{usuario}' está disponible.")