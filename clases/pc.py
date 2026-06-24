class pc:
    def __init__(self, head):
        self.head = head

    def add_pc(self, pokemon):
        nuevo = nodo(pokemon) 
        if pc.head is None:
            pc.head = nuevo
        else:
            actual = self.head

            while actual.next is not None:
                actual = actual.next

            actual.next = nuevo
    
    def replace(self):
        pass
        

class nodo:
    def __init__(self, pokemon):
        self.pokemon = pokemon # seria la data pero con otro nombre
        self.next = None
    


print(nodo)