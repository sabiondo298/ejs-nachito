lugares = ["paris", "little saint james", "monserrat", "la", "austria"]
def main():
    imprimir()

def imprimir():
    print(lugares)
    lista_ordenada = sorted(lugares)
    print(f"la lista ordenada es {lista_ordenada}")
    lista_ordenada_reves = sorted(lista_ordenada, reverse = True)
    print(f"la lista ordenada al reves es {lista_ordenada_reves}")

main()
