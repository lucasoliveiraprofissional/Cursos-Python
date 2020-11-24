'''Escreva um programa que faça o computador "pensar" em
um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.

Dei uma procurada tosca e vi que o randrange tem um range que podemos trabalhar
para delimitar o limite inferior e o limite superior de numeros que
vamos usar'''

import random

num= random.randrange(0, 5)

digit= int(input('Digite um número inteiro de 0 a 5: '))

if digit == num:
	print('\nVocê Venceu!')
else:
	print('\nVocê Perdeu.')

'''
código que eu fiz para testar se estava funcionando mesmo o rand:
while digit != num:
	digit= int(input('Digite um número inteiro de 0 a 5: '))
'''