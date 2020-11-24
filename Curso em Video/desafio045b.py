'''Crie um jogo que faça o computador jogar JoKenPo com você.'''

'''Peguei o que o professor fez, não gostei das opções que
eu encontrei.'''

from random import randint
from time import sleep
#sleep para perfumaria antes de acontecer a jogada

itens= ('Pedra', 'Papel', 'Tesoura')
computador= randint(0, 2)

print('Suas opções: \n'
      '[ 0 ] PEDRA\n'
      '[ 1 ] PAPEL\n'
      '[ 2 ] TESOURA\n')
jogador= int(input('Qual é a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)

print('-=' * 11)
print('\nO computador escolheu {}'.format(itens[computador]))
#ao invés de printar o número escolhido através do RandInt, ele printa
#o índice do item da tupla correspondente ao número escolhi do no RandInt.

print('O jodagor escolheu {}'.format(itens[jogador]))
print('-=' * 11)

if computador == 0: # computador jogou PEDRA
      if jogador == 0:
            print('EMPATE')
      elif jogador == 1:
            print('JOGADOR VENCE')
      elif jogador == 2:
            print('COMPUTADOR VENCE')
      else:
            print('JOGADA INVALIDA')

elif computador == 1: # computador jogou PAPEL
      if jogador == 0:
            print('COMPUTADOR VENCE')
      elif jogador == 1:
            print('EMPATE')
      elif jogador == 2:
            print('JOGADOR VENCE')
      else:
            print('JOGADA INVALIDA')

elif computador == 2: # compitador jogou TESOURA
      if jogador == 0:
            print('JOGADOR VENCE')
      elif jogador == 1:
            print('COMPUTADOR VENCE')
      elif jogador == 2:
            print('EMPATE')
      else:
            print('JOGADA INVALIDA')


