from math import sqrt, pow
class Retangulo:
    def __init__(self,largura,altura,cor):
        self.largura = largura
        self.altura = altura
        self.cor = cor

    def isSquare(self):
        return self.altura == self.largura
    
    def diagonal(self):
        return sqrt(pow(self.altura,2)+pow(self.largura,2))
    
    def perimetro (self):
        return 2 * self.altura + 2 * self.largura
    
    def mesmoPerimetro(self,r):
        return self.perimetro() == r.perimetro()
    
    def mesmaCor(self,r):
        return self.cor == r.cor
    
r1 = Retangulo(8,12,'Azul')
r2 = Retangulo(7,13,'Vermelho')

print(r1.isSquare())
print(r1.mesmoPerimetro(r2))
print(r1.mesmaCor(r2))
    