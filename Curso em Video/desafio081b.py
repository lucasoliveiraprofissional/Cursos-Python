'''Crie um programa que vai ler vários valores
e colocar em uma lista. Depois disso, mostre:

A)Quantos números foram digitados.

B)A lista de valores, ordenada de forma
decrescente.

C) Se o valor 5 foi digitado e está ou não
na lista.


Quis fazer versão b para ver a lógica dele'''

valores= []

while True:
    valores.append(int(input('Digite um valor: ')))
    resp= str(input('Quer continuar? [S/N] '))

    if resp in 'Nn':
        break

valores.sort(reverse=True)
print()
print(f'Voce digitou {len(valores)} elementos.')
print(f'Os valores em ordem decrescente são: {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não está na lista.')