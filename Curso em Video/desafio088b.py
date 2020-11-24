'''Faça um programa que ajude um jogador da
MEGA SENA a criar palpites. O programa
vai perguntar quantos jogos serão gerados
e vai sortear 6 números entre 1 e 60 para
cada jogo, cadastrando tudo em uma lista
composta.'''

'''Quis fazer versão b pois queria ver a
lógica dele e creio que ficou bem melhor
também o código.'''

'''Depois eu reparei que no meu código teve
a ocorrencia de no mesmo jogo repetirem
números. Isso não é legal.'''

from random import randint

lista= list()
jogos= list()

quant= int(input('Quantos jogos você quer que eu sorteie? '))
tot= 0

while tot <= quant:
    cont= 0
    while True:
        num= randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1

        if cont >= 6:
            break

    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
