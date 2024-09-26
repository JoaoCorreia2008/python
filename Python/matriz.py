notas_alunos = [
    ['Joao', 12.5,17.8],
    ['Vasco', 10.5,15.6],
    ['Filipe', 17.5,19.8],
    ['Hilario', 13.4,18.8]

]

# print(notas_alunos[1] [0])

for linha in range(4):
    for coluna in range (3):
        if coluna == 0:
            print(notas_alunos[linha][coluna], end =": ")
        elif coluna == 1:
            print(notas_alunos[linha][coluna], end=", ")
        else:
            print(notas_alunos[linha][coluna])

for c1,c2,c3 in notas_alunos:
    print(f'{c1}: {c2}, {c3}')

for linha in notas_alunos:
    print(f'{linha[0]}: {linha[1]}, {linha[2]}')