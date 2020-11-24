'''Crie um programa que gerencie o
aproveitamento de um jogador de
futebol. O programa vai ler o nome
do jogador e quantas partidas ele
jogou. Depois vai ler a quantidade
de gols feitos em cada partida.
No final, tudo isso será guardado
em um dicionário, incluindo o total
de gols feitos durante o campeonato.'''

'''Fiz versão B pois vacilei, 
demorei para praticar python'''

jogador= dict()
partidas= list()

jogador['nome'] = str(input('Nome do jogador: '))

tot= int(input(f"Quantas partidas o {jogador['nome']} jogou? "))

for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols na partida {c+1}?: ')))

jogador['gols'] = partidas[:]
'''Precisamos somar a quantidade de gols:'''

jogador['total']= sum(partidas)

'''Jeito 1 de printar:'''
print('\nResultado: ')
print(jogador)
print('')

'''Jeito 2 de printar:'''
for k, v in jogador.items():
    print(f'O campo {k} tem o valor: {v}')
print('')

'''Jeito 3 de printar: (ele vai tentar printar
sem usar a variavel tot.) O len funciona para 
os campos dos dicionarios tambem'''
print(f'O Jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')

