'''Faça um programa que jogue par ou impar
com o computador. O jogo só será
interrompido quando o jogador perder,
mostrando o total de vitorias consecutivas
que ele conquistou no final do jogo.'''

'''Parte baseado no desafio 045
desafio de jo ken po com o computador.'''

from random import randint
from time import sleep
#sleep para perfumaria antes de acontecer a jogada

vitorias= 0

while True:

    print('Suas opções: \n'
          '[ 0 ] PAR\n'
          '[ 1 ] ÍMPAR')
    jogador= int(input('Qual é a sua jogada? '))
    print('')

    while jogador < 0 or jogador > 1:
        print('Opção inválida! Veja as opções abaixo e digite novamente: ')
        print('Suas opções: \n'
              '[ 0 ] PAR\n'
              '[ 1 ] ÍMPAR')
        jogador = int(input('Qual é a sua jogada? '))
        print('')

    computador= randint(0, 10)

    numjogador= int(input('Digite um numero: '))

    print(f'Número escolhido pelo computador: {computador}')
    print('')

    print('-=' * 11)
    sleep(1)

    soma= computador + jogador
    divisao= soma % 2

    if divisao == 0 and jogador == 0:
        vitorias += 1
        print('Jogador Venceu!')
        print(f'Número de vitorias: {vitorias}')
        print('')

    elif divisao == 1 and jogador == 1:
        vitorias += 1
        print('Jogador Venceu!')
        print(f'Número de vitorias: {vitorias}')
        print('')

    elif divisao == 0 and jogador == 1:
        print('Jogador Perdeu!')
        break
        print('')

    elif divisao == 1 and jogador == 0:
        print('Jogador Perdeu!')
        break
        print('')
