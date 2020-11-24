'''Exercicio para casa, fiquei com preguiça de pensar
em como elaborar e peguei um da net'''

import random
print('Olá, bem-vindo ao nosso programa!')
print('Vamos ver se você vai ganhar um carro ou um bode')
print('')
acerto = random.randint(1,3)
bode = random.randint(1,3)
porta = int(input('Escolha a porta 1,2 ou 3: '))
x = porta
while 3 < porta >1:
    #Lucas: é a condição do jeito q não gosto de usar no while.
    #enquanto a porta digitada for maior que 3 ou menor que 1, faça:
    print('')
    print('Escolha inválida')
    porta = int(input('Escolha a porta 1,2 ou 3: '))
    print('')
print('')
print('Você escolheu a porta %d ' %porta)

while bode == acerto or bode == porta:
    bode = random.randint(1,3)

print('')
print('Mas eu te digo que na porta %d há um bode'%bode)
print('')
troca = int(input('Deseja trocar a porta? (1/Sim - 2/Não) :'))
if troca == 1:
    while porta == bode or porta == x:
        porta = random.randint(1,3)

if porta == acerto:
    print('')
    print('Parabéns!\nA porta %d é a porta premiada' %porta)
    print('Venha buscar seu carro!')
    print('')

else:
    print('')
    print('HUHeuHhuehuehHUEIHEU!')
    print('Na porta %d tem um  bode' %porta)
    print('')﻿

'''
1 ano atrás
jogo da porta bode kkk
    import random
    print("Bem vindo ao jogo das portas")
    porta = int(input("Escolha entre as portas 1,2 e 3: "))
    porta2 = 1
    portap = random.randint(1,3)
    portabode = random.randint(1,3)
    while portabode == portap or portabode == porta:
        portabode = random.randint(1,3)
    print("Voce escolheu a porta %i" %porta)
    print("Na porta %i tem um bode" %portabode)
    print("Voce deseja trocar de porta ?")
    resp = int(input("0 para nao e 1 para sim:"))
    if resp:
        while porta2 == porta or porta2 == portabode:
            porta2 = random.randint(1,3)
        if porta2 == portap:
            print("Parabens voce ganhou um carro!!")
        else:
            print("Parabens voce ganhou um bode")
    else:
        if porta == portap:
            print("Parabens voce ganhou um carro!!")
        else:
            print("Parabens voce ganhou um bode")﻿
'''

'''
from random import *

print("Olá, bem-vindo ao nosso programa! Vamos ver se você vai ganhar um carro ou não!")
porta = int(input("Escolha uma porta: "))
premio = randint(1, 3)

bode = randint(1, 3)
while bode == porta or bode == premio:
    bode = randint(1, 3)

print("\nEu lhe informo que na porta %i há um bode."%bode)
trocar = int(input("Deseja trocar de porta? (1 - Sim/0 - Não)"))

novaporta = randint(1, 3)
while novaporta == bode or novaporta == porta:
    novaporta = randint(1, 3)

if trocar == 1:
    porta = novaporta

if porta == premio:
    print("\nVocê ganhou um carro!")
else:
    print("\nInfelizmente você perdeu!")﻿
'''