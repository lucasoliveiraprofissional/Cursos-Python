'''Faça um programa que tenha uma função
chamada contador(), que receba três parâmetros:
início, fim e passo e realize a contagem.

Seu programa tem que realizar três contagens
através da função criada:

A) De 1 até 10, de 1 em 1
B) De 10 até 0, de 2 em 2
C) Uma contagem personalizada.'''

'''Fiz versão b pois travei para pensar
quando imaginei o if dentro da funcao
para determinar se iria ser decrescente
ou crescente.'''

from time import  sleep

def contador(i, f, p):
    '''Passo não pode ser negativo, mais detalhes
    no fim do programa. Agora verifica se é positivo
    ou negativo, ou se é igual a 0 também dá problema: '''

    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    print(f'Contade de {i} até {f} de {p} em {p}')
    sleep(2.5)

    if i < f:
        cont= i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('Fim!')

    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('Fim!')


#programa principal:
contador(1, 10, 1)
contador(10, 0, 2)

print('Agora é sua vez de personalizar a contagem')
ini= int(input('Inicio: '))
fim= int(input('Fim: '))
pas= int(input('Passo: '))

contador(ini, fim, pas)

'''Para a contagem personalizada, o passo precisa
ser sempre positivo, caso não seja, teremos um
loop infinito. Para isso, no começo é necessário
verificar se ele é positivo ou não e dar a 
tratativa necessária.'''