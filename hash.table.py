import json

from clase_pokemon import Pokemon

class hash_table:
    def __init__(self):
        self.table = {}

    def funcion_hash(self, key):
        return hash(key) % 151

    def insert(self, key, value):
        index = self.funcion_hash(key)
        if index not in self.table:
            self.table[index] = []
        self.table[index].append((key, value))

    def get(self, key):
        return self.table.get(key)

    def remove(self, key):
        if key in self.table:
            del self.table[key]

    def display(self):
        for key, value in self.table.items():
            print(f"{key}: {value}")

def load_pokemon_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def create_pokemon_hash_table(pokemon_data):
    pokemon_table = hash_table()
    for pokemon in pokemon_data:
        pokemon_table.insert(pokemon['id'], Pokemon(pokemon['id'], pokemon['nombre'], pokemon['tipo'], pokemon['poder']))
    return pokemon_table