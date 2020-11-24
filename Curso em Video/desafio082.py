'''Crie um programa que vai ler vários
números e colocar em uma lista.

Depois disso, crie duas listas extras
que vão conter apenas os valores pares
e os valores impares digitados,
respectivamente.

Ao final, mostre o conteúdo das três
listas geradas.'''

'''Fiz sem precisar usar o cont. Fiz em um laço só.'''

pares= []
impares= []
numeros= []

while True:
    numeros.append(int(input('Digite um valor: ')))
    n= numeros[len(numeros)-1]

    resp= str(input('Quer continuar? [S/N] '))

    if resp in 'Nn':
        if n % 2 == 0:
            pares.append(n)
        break

    if n % 2 == 0:
        pares.append(n)

    else:
        impares.append(n)

print(f'\nOs números digitados foram: {numeros}')
print(f'Os números pares digitados foram: {pares}')
print(f'Os números ímpares digitados foram: {impares}')