'''Variáveis Compostas - Dicionários'''

pessoas= {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas)

#printar só um elemento do dicionario pessoas:
print(pessoas['idade'])
print(pessoas['nome'])

#printar formatado:
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')

#printar as chaves:
print(pessoas.keys())

#mostrar os valores:
print(pessoas.values())

#mostrar os itens:
print(pessoas.items())

#acessar as chaves, itens e valores por laços:
#1 valores
for k in  pessoas.values():
    print(k)

#2 itens, para itens preciso colocar como parametro
#a chave e o valor:
for k, v in pessoas.items():
    print(f'{k} = {v}')

#enumerate usa-se em tuplas e listas.
#nos dicionarios usa-se os itens.

"""Caso deletemos um dos parametros do dicionário
e depois venhamos a pedir para printar, ele vai
printar somente os existentes."""

del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')

"""Caso façamos alguma alteração, será mostrado 
como ficou atualmente no print:"""

pessoas['nome']= 'Leandro'
for k, v in pessoas.items():
    print(f'{k} = {v}')

"""---------------------------"""

"""Dicionário dentro de lista: """

brasil= []
estado1= {'uf':'Rio de Janeiro', 'sigla': 'RJ'}
estado2= {'uf':'São Paulo', 'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)

print(estado1)

"""Printar a lista: """
print(brasil)

"""Printar somente um elemento do dicionário: """
print(brasil[0]['uf'])

"""---------------------------"""
"""Dicionário dentro de lista, porém incluindo
elementos através de for: """

estado= dict()
brasil= list()

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    print('')
    brasil.append(estado.copy())


"""Em dicionários temos que fazer cópia de elementos
sem utilizar do fatiamento, como nos casos anteriores,
onde usamos os [:]. Temos que usar o copy() e vai
funcionar sem problema algum."""

#printando agora:

for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')

#ou:
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()