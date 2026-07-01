import json
def cargar_medallas(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

class hash_set():
    def __init__(self):
        self.tabla = []

    def add(self, llave):
        if llave not in self.tabla:
            self.tabla.append(llave)

    def __iter__(self):
        return iter(self.tabla) # lo uso para poder iterar en las medallas del jugador

    def mostrar(self):
        print(self.tabla)

def ver_medallas():
    medallas = cargar_medallas('medallas.json')
    return medallas

