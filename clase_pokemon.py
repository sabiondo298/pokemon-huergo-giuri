class pokemon:
    def __init__(self,id,nombre,tipo,poder):
        self.id=id
        self.nombre=nombre
        self.tipo=tipo
        self.poder=poder

mi_pokemon = pokemon(1,"Pikachu","Electrico",100)
print(mi_pokemon.__dict__)