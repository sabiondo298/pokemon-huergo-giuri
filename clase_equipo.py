class Equipo:
    def __init__(self, size, pokemones=None):
        if pokemones is None:
            pokemones = []
        self.size = size
        self.pokemones = pokemones

    def add(self, pokemon):
        if len(self.pokemones) < self.size:
            self.pokemones.append(pokemon)
        else:
            print("El equipo ya está lleno. El pokemon atrapado ira a la PC, la puedes acceder desde el menu.")

    def display(self):
        print(f"Equipo: {self.pokemones}")


