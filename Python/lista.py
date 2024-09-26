import os
ferramentas = ['Alicate', 'Martelo','Chave de fendas','Serra']

# print(ferramentas[0])
ferramentas[2] = 'Parafusadeira'
# print(ferramentas [2])
# print(ferramentas)
# print(type(ferramentas))
# Adicionar elemento no final da lista 
ferramentas.append('Chave de fendas')
# print(ferramentas)
ferramentas.insert(1,'furradeira')
# print(ferramentas)
# os.system('cls')
# for fr in ferramentas:
#     if fr.startswith(('C','P')):
#         print(f'x {fr}')

#Remover o ultimo elemento da lista
ferramentas.pop()
print(ferramentas)
#Remover um elemento específico
ferramentas.pop(2)
print(ferramentas)


ferramentas.remove('Serra')
print(ferramentas)