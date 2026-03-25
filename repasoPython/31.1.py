from random import randint

class Die:
    def __init__(self, num_lados=6):
        self.num_lados = num_lados

    def roll_die(self):
        for i in range(10):
            random_num = randint(1, self.num_lados)
            print(random_num)

if __name__ == "__main__":
    dado6 = Die(6)
    print("Lanzando un dado de 6 lados:")
    dado6.roll_die()

    dado10 = Die(10)
    print("\nLanzando un dado de 10 lados:")
    dado10.roll_die()

    dado20 = Die(20)
    print("\nLanzando un dado de 20 lados:")
    dado20.roll_die()


