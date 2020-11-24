'''Crie um programa que vai ler vários valores
e colocar em uma lista. Depois disso, mostre:

A)Quantos números foram digitados.

B)A lista de valores, ordenada de forma
decrescente.

C) Se o valor 5 foi digitado e está ou não
na lista.'''

numeros= []
cont= 0
esta5= False

while True:
    n= int(input('Digite um valor: '))
    numeros.append(n)
    cont= 0

    if 5 in numeros:
        #pos[cont]= (str(numeros).index(5)+1)
        esta5= True

    r= str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r in 'Nn':
        break

numeros.sort(reverse=True)
print(f'\nVocê digitou {cont} numeros.')
print(f'Na ordem decrescente, voce digitou os valores: {numeros}')

if esta5 == True:
    print('O número 5 foi digitado.')
else:
    print('O número 5 não foi digitado')