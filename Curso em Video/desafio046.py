'''Faça um programa que mostra na tela uma contagem
regrssiva para o estouro de fogos de artifício,
indo de 10 até 0, com uma pausa se 1 segundo entre eles.'''

from time import sleep

for cont in range(10, -1, -1):
    print(cont)
    sleep(1)

print('Fim')

