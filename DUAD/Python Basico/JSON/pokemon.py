import json

def read_pokemones(filename):
    # abre y lee el archivo, RETORNA la lista
    with open(filename, "r") as file:
        return json.load(file)

def get_new_pokemon():
    # pide los datos, RETORNA el diccionario del nuevo pokemon
    name = input("pokemon name: ")
    type_ = input("pokemon type: ")
    return {"name": name, "type": type_}

def add_pokemon(pokemones, new_pokemon):
    # agrega el nuevo a la lista, RETORNA la lista actualizada
    pokemones.append(new_pokemon)
    return pokemones

def save_pokemones(filename, pokemones):
    # guarda la lista en el archivo
    with open(filename, "w") as file:
        json.dump(pokemones, file, indent=4)

def main():
    # aquí se llaman las 4 funciones EN ORDEN
    pokemones = read_pokemones("pokemones.json")
    new_pokemon = get_new_pokemon()
    pokemones = add_pokemon(pokemones, new_pokemon)
    save_pokemones("pokemones.json", pokemones)
    print("pokemon agregado!")

main()