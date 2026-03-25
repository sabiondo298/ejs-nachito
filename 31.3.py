from random import randint
loteria = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e"]
numeros_ganadores = []
my_ticket = []
intentos = 0

for i in range(4):
    numero = loteria[randint(0, len(loteria)-1)]
    numeros_ganadores.append(numero)

print("Números y letras ganadoras:", numeros_ganadores)

def girar():
    global intentos
    my_ticket = [] 
    for i in range(4):
        numero = loteria[randint(0, len(loteria)-1)]
        my_ticket.append(numero)
    print("Tu ticket es:", my_ticket)
    intentos += 1
    return my_ticket


while True:
    my_ticket = girar()
    if my_ticket == numeros_ganadores:
        break

print(f"¡Felicidades! Has ganado después de {intentos} intentos. Los números ganadores eran: {numeros_ganadores}")


