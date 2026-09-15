import json

data = json.loads('{"name": "Alice", "age": 30}')
# text = json.dumps(data, indent=2)
archivo = "prueba.json"
with open(archivo, "w") as file:
    # file.write(text)
    json.dump(data, file, indent=2)

# ------------- Hacen lo mismo ------------------------

# import json

# data = json.loads('{"name": "Alice", "age": 30}')
# text = json.dumps(data, indent=2)

# with open(archivo, "w") as file:
#     file.write(text)