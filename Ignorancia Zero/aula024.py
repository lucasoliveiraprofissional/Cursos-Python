'''Numeros pseudo aleatorios, modulo random'''

import random

# a cada execução do for, indo até 10, ele pega e printa um numero aleatorio
#entre 1 e 6
'''
for i in range(10):
    x= random.randrange(1,7)
    print(x)
'''

# a cada execução do for, indo até 10, ele pega e printa um numero aleatorio
#entre 1 e 6, MAS com passo 2, ou seja, 1, ou 3 ou 5

'''
for i in range(10):
    x= random.randrange(1, 7, 2)
    print(x)
'''

#rand int vai pegar o numero 7
'''
for i in range(10):
    x= random.randint(1, 7)
    print(x)
'''

#random choice escolhe numeros dentro de
#uma sequencia de numeros que determinamos
#aí não precisamos usar o range como parametro
#do random
'''
for i in range(10):
    x= random.choice([1, 2, 3, 4, 5, 6])
    print(x)
'''

#random retornar numero real
'''
for i in range(10):
    print(random.random())
'''

#random uniform voce escolhe o intervalo
#de numeros reais que quer receber
'''
for i in range(10):
    x= random.uniform(1, 7)
    print(x)
'''
