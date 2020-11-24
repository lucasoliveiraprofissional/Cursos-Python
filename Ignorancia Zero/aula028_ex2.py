'''Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e
armazene os resultados em um vetor. Depois, mostre quantas vezes cada valor
foi conseguido.'''


import random
'''
vetor= []
for i in range(100):
    vetor.append(random.randint(1, 6))

for i in range(1, 7):
    print('A face {} apareceu {} vezes'.format(i, vetor.count(i)))
'''
'''O dado foi jogado 100 vezes, os resultados de cada vez que ele foi jogado
foram armazenados no vetor e depois, mostra-se na tela quantas vezes o dado
parou com o nº1 para cima, quantas vezes o 2... até o 6'''

'''Depois do desafio inicial, ele quis fazer com que o usuário determinasse o numero
de vezes que o dado seria jogado.'''

n= int(input('Digite o numero de lancamentos: '))
print('\n')

vetor= []
for i in range(n):
    vetor.append(random.randint(1, 6))

for i in range(1, 7):
    print('A face {} apareceu {:.2f}% das vezes'.format(i, (100 * vetor.count(i)) / n))