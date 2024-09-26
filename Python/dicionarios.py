aluno = {
    'nome': 'Joao',
    'nota_matematica': 12.4,
    'nota_portugues' : 13.25,
    'outras_notas': [14,20,15.5,9.5]

}

print(aluno['outras_notas'][1])

for k in aluno.values(): #Imprime a chave
    print(k)
print('-----------------------------------)')

for v in aluno.values(): #Imprime os valores
    print(v)

print('-----------------------------------)')
for k,v in aluno.items():
    print(f'{k}: {v}')

alunos = [
    {   
    'nome': 'Joao',
    'nota_matematica': 12.4,
    'nota_portugues' : 13.25,
    'outras_notas': [14,20,15.5,9.5]
    },
    {'nome': 'leonardo',
    'nota_matematica': 10.4,
    'nota_portugues' : 10.25,
    'outras_notas': [10,10,13.5,0.5]
    }
]
print(alunos[1]['nome'])

nomes = ['Joao','leonardo']
print(nomes[0][2])

nome = 'Joao'
nome = ['J','o','a','o']