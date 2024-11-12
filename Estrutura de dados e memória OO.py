class Pilha:
    def __init__(self, max_size):
        self.max_size = max_size 
        self.pilha = []

    def push(self, elemento):
        if len(self.pilha) >= self.max_size:
            print(f"Erro: A pilha está cheia. Não é possível adicionar o elemento {elemento}.")
        else:
            self.pilha.append(elemento)
            print(f"{elemento} adicionado à pilha.")

    def pop (self):
        if self.is_empty():
            print("Erro: A pilha está vazia. Não é possível remover um elemento.")
        else:
            elemento = self.pilha.pop()
            print(f"{elemento} removido da pilha.")
            return elemento

        def peek (self):
            if self.is_empty():
                print("Erro: A pilha está vazia. Não há elementos para mostrar.")
            else:
                print(f"Elemento no topo da pilha: {self.pilha[-1]}")

                def is_empty(self):
                    return len(self.pilha) == 0
                
                def estado_atual(self):
                    if self.is_empty():
                        print("A pilha está vazia.")
                    else:
                        print(f"Pilha atual: {self.pilha}")
minha_pilha = Pilha(3)

minha_pilha.push(10)
minha_pilha.push(20)
minha_pilha.push(30)
minha_pilha.push(40)

minha_pilha.estado_atual()
minha_pilha.pop()
minha_pilha.peek()

minha_pilha.estado_final()
                    

                                        