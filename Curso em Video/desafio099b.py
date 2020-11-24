'''Faça um programa que tenha uma função
chamada maior(), que receba vários
parâmetros com valores inteiros.

Seu programa tem que analisar todos os
valores e dizer qual deles é o maior.'''

'''Fiz a versão b pois a proposta dele para esse 
exercício é bem diferente do que eu pensava,
pois já fui fazendo sem ver como exatamente
ele queria.'''

from time import sleep

def maior(*num):
    cont= maior= 0
    print('\nAnalisando os valores passados... ')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior= valor
        else:
            if valor > maior:
                maior= valor
        cont += 1

    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')

#programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 9)
maior(1, 2)
maior(6)
maior()