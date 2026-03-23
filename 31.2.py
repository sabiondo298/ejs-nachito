from random import randint
loteria = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e"]
print("Números y letras ganadoras:")
for i in range(4):
    print(loteria[randint(0, len(loteria)-1)])