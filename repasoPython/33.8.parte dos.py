import json

with open('numero_favorito.json', 'r') as f:
    num_fav = json.load(f)

print(f"¡Sé cuál es tu número favorito! Es {num_fav}.")