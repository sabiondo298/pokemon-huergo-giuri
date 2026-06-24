class Pokemon:
    def __init__(self,id,nombre,tipo,poder):
        self.id=id
        self.nombre=nombre
        self.tipo=tipo
        self.poder=poder

    def __repr__(self):
        return (f"Pokemon(ID: {self.id}, nombre: {self.nombre}, tipo: {self.tipo}, poder: {self.poder})")

