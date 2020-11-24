'''Escreva um programa que leia um numero
n inteiro qualquer o mostre na tela os n
primeiros elementos de uma sequencia de
fibonacci'''


'''começando normalmente por 0 e 1,
na qual, cada termo subsequente
corresponde à soma dos dois
anteriores.'''

'''Vou precisar fazer desafio063b.
Tentei pensar no algoritmo fibonacci
em Python e não consegui.'''


elementos= int(input('Quantos elementos da sequencia voce quer ver? '))

primeiro= 0

segundo= 1

while segundo <= elementos:
    if segundo == 1:
        print('{} → '.format(segundo), end='')
        aux= segundo
        segundo+= aux
    print('{} → '.format(segundo), end='')
    segundo+= segundo
