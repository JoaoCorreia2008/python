from math import sqrt

class Triangulo:
    def __init__(self,lado1=0,lado2=0,lado3=0):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def isTriangle(self):
        return self.lado1 < self.lado2 + self.lado3 and self.lado2 < self.lado1 + self.lado3 and self.lado3 < self.lado1 + self.lado2
    def perimeter(self):
            return self.lado1 + self.lado2 + self.lado3
    def area(self):
        sp = self.perimeter() / 2
        return sqrt(sp*(sp-self.lado1)*(sp-self.lado2)*(sp-self.lado3)) 
    def tipo(self):
         if self.lado1 == self.lado2 == self.lado3:
              return "Equilátero"
         if self.lado1 != self.lado2 and self.lado2 != self.lado3 and self.lado1 != self.lado3:
              return "Escaleno"
         return"Isósceles"
tr1 = Triangulo(8,11,12)

if (tr1.isTriangle()):
     print(f'Perimetro =  {tr1.perimeter()}')
     print(f'Area =  {tr1.area()}')
     print(f'Tipo =  {tr1.tipo()}')
