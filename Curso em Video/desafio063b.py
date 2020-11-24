'''Escreva um programa que leia um numero
n inteiro qualquer o mostre na tela os n
primeiros elementos de uma sequencia de
fibonacci'''

'''Precisei fazer desafio063b.
Tentei pensar no algoritmo fibonacci
em Python e não consegui.'''

n= int(input('Quantos termos voce quer mostrar? '))

t1= 0
t2= 1

print('{} → {}'.format(t1, t2), end='')

cont= 3
#vai começar desse modo pois já temos os
#termo 1 e 2

while cont <= n:
    t3= t1 + t2
    print(' → {}'.format(t3), end='')
    cont += 1
    t1= t2
    t2= t3
    #para fazer com que os termos vão andando
    #e pegando sempre o proximo valor.
print(' → Fim')
