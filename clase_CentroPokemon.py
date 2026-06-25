class CentroPokemon:
    def __init__(self, pokemon=None):
        self.pokemon = pokemon

    def curar(self, pokemon):
        nombre = getattr(pokemon, "nombre") # lo uso para que llege el nombre como string a main.
        print(f"Tu pokémon: {nombre} ha sido curado.")
