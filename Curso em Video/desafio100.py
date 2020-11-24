'''Faça um programa que tenha uma lista
chamada números e duas funções chamadas
sorteia() e somaPar(). A primeira função
vai sortear 5 números e vai colocá-los
dentro da lista e a segunda função vai
mostrar a soma entre todos os valores
PARES sorteados pela função anterior.'''

from random import randint

numeros= list()

c= 0

def sorteia(numeros):
    print(f'Sorteando os números: ', end='')
    for c in range(0, 5):
        numeros[c] = randint(0, 9)
        somaPar(numeros)
        print(f'{numeros[c]}, ')


def somaPar(numeros):
    acum= 0
    if numeros[c] % 2 == 0:
        acum=+ numeros[c]

    print(f'A soma de todos os valores pares é: {acum}')

sorteia(numeros)
somaPar(numeros)