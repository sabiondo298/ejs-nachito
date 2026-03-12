invitados = ["kobe", "omar", "la coqueta"]
print(f"{invitados} estan invitados")
print("la coqueta no pudo venir")
invitados[-1] = "el pepe"
print(f"{invitados} estan invitados")
print("consegui una mesa mas grande wacho")
invitados.insert(0, "la papa")
invitados.insert(2, "bejamin nethyahiu")
invitados.insert(-1, "el mencho")
print(f"{invitados} estan invitados")

print("se me rompio la mesa, solo pueden venir 2 personas")
for i in range(4):
    invitado_eliminado = invitados.pop(-1)
    print(f"{invitado_eliminado} no puede venir")

print(f"{invitados} estan invitados")
del invitados[0]
del invitados[0]
print(invitados)