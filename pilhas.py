class Pilha():
    def __init__(self):
        self.data = []
        
    def push(self, x): #empilha um elemento
        self.data.append(x)
        
    def pop(self): #desempilha um elemento
        if len(self.data) > 0:
            return self.data.pop(-1)
        
    def top(self): #acessa o elemento do topo, sem desempilhá-lo
        if len(self.data) > 0:
            return self.data[-1]
        
    def empty(self): #verifica se a pilha está vazia
        return len(self.data) > 0