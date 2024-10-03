# João Correia  14597
#Exercicio 1
n=0
def somar(*args):
    soma = 0
    for arg in args:
        if 5 < arg < 10:
            soma = soma + arg
    return soma
print(somar(7,8,9))


# Exercicio 2
par = lambda x: "P" if 0 < x > 0 else "N"
print(par(9))

# Exercicio 3 
def inverter(num):
    inverso = 0
    while num != 0:
        inverso = inverso * 10 + num % 10
        num = num // 10
    return inverso
print(inverter(1234596678))


# Exercicio 4
contar_digitos = lambda num: len(str(num))
numero = int(input("Digite um valor : "))
print(contar_digitos(numero))

# Exercicio 5

def perfeito (num):
    soma = 0
    for divisor in range(1,num):
        if num % divisor == 0:
            soma = soma + divisor
    if num == soma:
        print("Perfeito")
    else:
        print("Imperfeito")
perfeito(6)
perfeito(7)
perfeito(99)
perfeito(3)