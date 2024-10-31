class A: #super class
    atributo_a = 'Valor de a'

    def __init__(self,atributo):
        self.atributo = atributo
    
    def metodo(self):
        print('Valor A',self.__class__.__name__)

class B(A): # sub class o B recebe tudo que esta na class A, tem acesso ao atributo do a 
    atributo_b = 'Valor de b'

    def __init__(self,atributo, atributoB , outra_coisa):
        super().__init__(atributo,atributoB)
        self.outra_coisa = outra_coisa
    
    def metodo(self):
        print('Valor B',self.__class__.__name__)

x = A('Novo valor')
y = B('Novo valor B','Outra coisa qualquer')

# print(x.atributo_a)
# print(x.atributo)
# x.metodo()
print(y.atributo_a)
x.metodo()
y.metodo()
# help(y)
print(B.mro())