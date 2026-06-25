import json

from clase_pokemon import Pokemon

class HashTable:
    def __init__(self):
        self.tabla = [[] for _ in range(152)]

    def funcion_hash(self, llave):
        return llave % 152 

    def insert(self, llave, valor):
        indice = self.funcion_hash(llave)
        self.tabla[indice].append([llave, valor])

    def get(self, llave):
        indice = self.funcion_hash(llave)

        for elemento in self.tabla[indice]:
            if elemento[0] == llave:
                return elemento[1]

        return None


    def display(self):
        for pokemon in self.tabla:
            print(f"{pokemon}")



def cargar_pokemon_data(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        data = json.load(file)
    return data

def crear_pokemon_hash_table(pokemon_data):
    pokemon_table = HashTable()
    for pokemon in pokemon_data:
        pokemon_table.insert(pokemon['id'], Pokemon(pokemon['id'], pokemon['nombre'], pokemon['tipo'], pokemon['poder']))
    return pokemon_table

if __name__ == "__main__":
    pokemon_data = cargar_pokemon_data('pokemon_data.json')
    pokemon_table = crear_pokemon_hash_table(pokemon_data)
    pokemon_table.display()
    
    