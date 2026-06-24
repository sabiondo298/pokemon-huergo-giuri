class equipo:
    def __init__(self, size, pokemones):
        size = 6
        self.size = size
        self.pokemones = pokemones

    def __add__(self, pokemones):
        if len(self.pokemones) < self.size:
            self.pokemones.append(pokemones)
        else:
            print("El equipo ya está lleno. El pokemon atrapado ira a la PC, la puedes acceder desde el menu.")

    def __display__(self):
        return (f"Equipo: {self.pokemones}")