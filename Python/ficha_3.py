# 1. Crie uma lista com os números pares de 1 a 10.
lista_par=[
    n
    for n in range(1,11) # range cria uma lista que vai de 1 a 11 mas o 11 n faz parte 
    if n % 2 == 0 
]
print(lista_par)

# 2. Crie uma lista com os quadrados dos números de 1 a 10.
nums=[1,2,3,4,5,6,7,8,9,10]
lista02 = [
    n*n
    for n in nums
]
print(lista02)

# 3. Dada uma lista de palavras, crie uma nova lista que indique o tamanho de cada palavra.

palavras = ['Jogo',"Rizz","Hoje",'Oficina']
lista03 = [
    len(p)
    for p in palavras # o p agora é as palavras que estao na lista 
]
print(lista03)

# 4. Dada uma lista de números, crie uma lista apenas com os números maiores que 5.
nums=[1,2,3,4,5,6,7,8,9,10]
lista04 = [
    num
    for num in range(11)
    if num > 5
]
print(lista04)

# 5. Crie uma lista com as letras maiúsculas de uma string. (nome = 'MarcelO ViEiRa amorIM')

nome = 'JoAo AfonSo MArqUes COrReIa'
lista05 =[
    
    l for l in nome if l.isupper()
]
print(lista05)
# 6. Dada uma lista de números, crie uma nova lista onde se o número for múltiplo de 3, é apresentado o dobro deste caso contrário aparece o mesmo número da lista original.
multiplos = [
    n*2 if n % 3 == 0 else n 
    for n in nums
]
print(multiplos)

# 7. Dada uma lista de nomes, crie uma nova lista apenas com os nomes que começam com a letra "A". Todos os nomes da nova lista devem aparecer em maiúsculas.

# 8. Dada uma lista de frutas, crie uma nova lista com o comprimento de cada fruta, apenas para as frutas com mais de 5 letras. Caso contrário, deve aparecer 0.


