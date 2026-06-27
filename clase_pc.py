class PC:
    def __init__(self, head=None):
        self.head = head

    def add_pc(self, pokemon):
        nuevo = nodo(pokemon)
        if self.head is None:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next is not None:
                actual = actual.next
            actual.next = nuevo
    
    def display(self):
        if self.head is None: #si esta vacia returnea eso
            print("PC vacío")
            return

        actual = self.head
        indice = 1
        while actual is not None:
            nombre = getattr(actual.pokemon, "nombre")
            print(f"{indice}. {nombre}")
            actual = actual.next
            indice += 1


class nodo:
    def __init__(self, pokemon):
        self.pokemon = pokemon # seria la data pero con otro nombre
        self.next = None
    


print(nodo)