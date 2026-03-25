names = []

while True:
    name = input("Pone tu nombre (apreta enter para terminar): ")
    if name == "":
        break
    names.append(name)

with open("guest_book.txt", "w") as file:
    for name in names:
        file.write(name + "\n")
