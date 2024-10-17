dados = [
    {'nome': 'Marcelo', 'sexo': 'M', 'altura': 1.84, 'peso': 98},
    {'nome': 'Rui', 'sexo': 'M', 'altura': 1.94, 'peso': 83},
    {'nome': 'Joana', 'sexo': 'F', 'altura': 1.68, 'peso': 68},
    {'nome': 'Leonor', 'sexo': 'F', 'altura': 1.64, 'peso': 59},
    {'nome': 'Alfredo', 'sexo': 'M', 'altura': 1.87, 'peso': 105}
]

# 1a
sexo_binario = list(map(lambda x: 1 if x['sexo'] == 'M' else 0, dados))
print("1a: ", sexo_binario)

# 1b
nome_sexo_binario = list(map(lambda x: (x['nome'], 1 if x['sexo'] == 'M' else 0), dados))
print("1b: ", nome_sexo_binario)

# 1c
imc_dados = tuple(map(lambda x: (x['nome'], x['peso'] / (x['altura'] ** 2)), dados))
print("1c: ", imc_dados)

# 2
def media_peso_altura(dados):
    total_peso = sum(map(lambda x: x['peso'], dados))
    total_altura = sum(map(lambda x: x['altura'], dados))
    return (total_peso / len(dados), total_altura / len(dados))

media = media_peso_altura(dados)
print("2: ", media)