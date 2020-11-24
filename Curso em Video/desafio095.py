'''Aprimore o DESAFIO093 para que ele
funcione com vários jogadores, incluindo
um sistema de visualização de detalhes
do aproveitamento de cada jogador.'''

time= list()
jogador= dict()
partidas= list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))

    tot= int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
    partidas.clear()

    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1}?: ')))

    jogador['gols'] = partidas[:]
    '''Precisamos somar a quantidade de gols:'''

    jogador['total']= sum(partidas)
    time.append(jogador.copy())

    while True:
        resp= str(input('Você quer continuar? [S/N] ')).upper()
        if resp in 'SN':
            break
        print('Digite corretamente!')

    if resp == 'N':
        break

print('')
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print('')
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')

while True:
    busca= int(input('Mostrar dados de qual jogador? '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Não exist jogador com código {busca}')
    else:
        print('')
        print(f' Levantamento do jogador: {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f' No jogo {i+1} fez {g} gols.')