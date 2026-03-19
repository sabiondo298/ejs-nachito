pediddos_sandguche = ["milanga", "jamon Y queso", "lomito", "hamburguesa", "veggie"]
sanguches_terminados = []
while pediddos_sandguche:
    pedido = pediddos_sandguche.pop()
    print(f"Estoy preparando tu {pedido}...")
    sanguches_terminados.append(pedido)
print("Los siguientes sanguches están listos:")
for sanguche in sanguches_terminados:
    print(f"- {sanguche}")