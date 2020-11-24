'''Escreva um programa que faça o computador "pensar" em
um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.

Fazendo de acordo com o Guanabara
Quis fazer assim pois eu acho que a resolução dele será muito melhor'''

from random import randint

computador= randint(0,5)
#print('Pensei no número {}'.format(computador))

jogador = int(input('Em que número eu pensei? '))

if jogador == computador:
    print('Você ganhou!')
else:
    print('Eu ganhei! Eu pensei no número {} e não no {}!'.format(computador,jogador))
