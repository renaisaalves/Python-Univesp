class Pilha():
    def __init__(self, pilha):
        self.data = pilha
        
    def push(self, x): #empilha um elemento
        self.data.append(x)
        
    def pop(self): #desempilha um elemento
        if len(self.data) > 0:
            return self.data.pop(-1)
        
    def top(self): #acessa o elemento do topo, sem desempilhá-lo
        if len(self.data) > 0:
            return self.data[-1]
        
    def empty(self): #verifica se a pilha está vazio
        return len(self.data) > 0

lista = [2, 4, 5, 8, 10]
pilha = Pilha(lista)
print(lista.empty())
class Gato():
    def __init__(self, animal):
        self.nome = animal
        print(f'Seu gato se chama {self.nome}')
        
nome_gato = str(input('Digite o nome do seu gato: '))
g1 = Gato(nome_gato)