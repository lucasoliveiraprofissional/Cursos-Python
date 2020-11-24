'''Faça um programa que ajude um jogador da
MEGA SENA a criar palpites. O programa
vai perguntar quantos jogos serão gerados
e vai sortear 6 números entre 1 e 60 para
cada jogo, cadastrando tudo em uma lista
composta.'''

from random import randint

jogos= []

perg= int(input('Quantos jogos você quer que eu sorteie? '))
print('')

for c in range(0, perg):
    for jog in range(0, 6):
        jogos.append(randint(1, 60))

    print(F'Jogo {c+1}: {jogos}')
    jogos.clear()
print('\nFim.')