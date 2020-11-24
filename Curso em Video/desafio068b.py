'''Faça um programa que jogue par ou impar
com o computador. O jogo só será
interrompido quando o jogador perder,
mostrando o total de vitorias consecutivas
que ele conquistou no final do jogo.'''

'''Parte baseado no desafio 045
desafio de jo ken po com o computador.'''

'''Quis ver a solução dele, mas creio que
a minha ficou melhor em alguns pontos.'''

from random import randint
v= 0

while True:
    jogador= int(input('Diga um valor: '))
    computador= randint(0, 10)
    total= jogador + computador
    tipo= ' '

    while tipo not in 'PI':
        tipo= str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]

    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total}', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')

    if tipo == 'P':
        if total % 2 == 0:
            print('Voce VENCEU!')
            v += 1
        else:
            print('Voce PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce VENCEU!')
            v += 1
        else:
            print('Voce PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Voce teve {v} vitorias!')
