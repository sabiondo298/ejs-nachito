import json

num_fav = int(input("¿Cuál es tu número favorito? "))
with open('numero_favorito.json', 'w') as f:
    f.write(json.dumps(num_fav))