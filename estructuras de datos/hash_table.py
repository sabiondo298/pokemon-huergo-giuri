import json

from clase_pokemon import Pokemon

class hash_table:
    def __init__(self):
        self.tabla = {}

    def funcion_hash(self, llave):
        return hash(llave) % 151 # numero de buckets en mi hash map

    def insert(self, llave, value):
        index = self.funcion_hash(llave)    # hashea la llave para obtener el indice del bucket
        if index not in self.tabla:
            self.tabla[index] = []                  # esto le asigna una lista vacia al indice del bucket si no existe
        self.tabla[index].append((llave, value))    # y despues le agrega un valor a esa lista 

    def get(self, llave):
        index = self.funcion_hash(llave) # hashea la llave para obtener el indice del bucket
        entries = self.tabla.get(index)
        if not entries:
            return None # si no hay entradas en ese bucket, devuelve None
        for k, v in entries:    # recorre las entradas en ese bucket para encontrar la llave y devolver su valor
            if k == llave:      # si la llave es igual al valor que estamos buscando, devuelve el valor asociado a esa llave
                return v
        return None


    def display(self):
        for llave, value in self.tabla.items():
            print(f"{llave}: {value}")

def cargar_pokemon_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def crear_pokemon_hash_table(pokemon_data):
    pokemon_table = hash_table()
    for pokemon in pokemon_data:
        pokemon_table.insert(pokemon['id'], Pokemon(pokemon['id'], pokemon['nombre'], pokemon['tipo'], pokemon['poder']))
    return pokemon_table

if __name__ == "__main__":
    pokemon_data = cargar_pokemon_data('pokemon_data.json')
    pokemon_table = crear_pokemon_hash_table(pokemon_data)
    
    