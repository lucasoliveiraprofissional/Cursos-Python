'''Faça um programa que tenha uma lista
chamada números e duas funções chamadas
sorteia() e somaPar(). A primeira função
vai sortear 5 números e vai colocá-los
dentro da lista e a segunda função vai
mostrar a soma entre todos os valores
PARES sorteados pela função anterior.'''

'''Fiz a versão b pois a minha ficou parecida
porém não funcionou, e porque queria ver como
ele faria.'''

from random import randint
from time import sleep

def sorteia(lista):
    print(f'Sorteando os números: ', end='')

    for cont in range(0, 5):
        n= randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)

    print('Pronto')


def somaPar(lista):
    soma= 0

    for valor in lista:
        if valor % 2 == 0:
            soma += valor

    print(f'A soma dos valores pares do vetor {numeros} é {soma}')

numeros= list()
sorteia(numeros)

somaPar(numeros)