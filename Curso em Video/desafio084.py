'''Faça um programa que leia nome e peso
de várias pessoas, guardando tudo em uma
lista. No final, mostre:

A) Quantas pessoas foram cadastradas.

B) Uma listagem com as pessoas mais pesadas.

C) Uma listagem com as pessoas mais leves.'''

pessoas= list()
pesados= list()
leves= list()
#nome= list()
#peso= list()
cont= 0
maior= menor= 0.0

while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))

    if cont == 0:
        maior = pessoas[1]
        menor= pessoas[1]

    if pessoas[1] > maior:
        maior= pessoas[1]

    if pessoas[1] < menor:
        menor= pessoas[1]

    cont += 1

    resp= str(input('Continuar? [S/N] ')).upper().strip()[0]
    if resp in 'Nn':
        break

for p in pessoas:
    if float(p[1]) == menor:
        leves.append(p[0])

    if float(p[1]) == maior:
        pesados.append(p[0])

print(f'\nAo todo, você cadastrou {cont} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de {pesados}')
print(f'O menor peso foi de {menor}Kg. Peso de {leves}')
