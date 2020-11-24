'''Crie um programa que vai gerar 5 números
aleatórios e colocar em uma tupla.

Depois disso, mostre a listagem de numeros
gerados e também indique o menor e o maior
valor que estão na tupla.'''

'''Esse programa é direto a versão b pois eu
não tinha ideia de que daria para fazer o que
dá para fazer nesse programa'''

from random import randint

numeros= {randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)}

print('Os valores sorteados foram: ', end='')

for n in numeros:
    print(f'{n}', end=' ')

print(f'\nO maior número é: {max(numeros)}')
print(f'O menor número é: {min(numeros)}')