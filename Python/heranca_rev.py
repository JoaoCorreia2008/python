class Forma:
    def __init__(self,numlados,cor):
        self.numlados = numlados
        self.cor = cor
    
    def escrever(self):
        print(f'Método da classe Forma')
    
class Quadrado(Forma):
    def __init__(self, numlados, cor,diagonal):
        super().__init__(numlados, cor)
        self.diagonal = diagonal
    
    def escrever(self):
        print(f'Método da classe Quadrado')

q= Quadrado(4,'Azul',True)
q.escrever()
f = Forma (3,'Amarelo')
f.escrever()