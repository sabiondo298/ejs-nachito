import json

try:
    with open('numero_favorito.json', 'r') as f:
        num_fav = json.load(f)
    print(f"¡Sé cuál es tu número favorito! Es {num_fav}.")
except (FileNotFoundError, json.JSONDecodeError):
    num_fav = int(input("¿Cuál es tu número favorito? "))
    with open('numero_favorito.json', 'w') as f:
        f.write(json.dumps(num_fav))