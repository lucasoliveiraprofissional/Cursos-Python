'''Crie um programa que leia o nome e o
preço de vários produtos. O programa
deverá perguntar se o usuário vai continuar.
No final, mostre:

A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1.000,00.
C) Qual é o nome do produto mais barato. '''

'''O maior e menor, como já estava pronto,
eu peguei do desafio065'''

pergunta= ''
soma= 0
maismil= 0
nomebarato= ''

maior= 0
menor= 0

cont= 0

while True:
    nomeprod= str(input('Digite o nome do produto: '))
    preco= float(input('Digite o preço do produto: '))

    soma += preco

    if preco > 1000:
        maismil += 1

    if cont == 0:
        maior= menor= preco

    else:
        if preco > maior:
            maior= preco

        if preco < menor:
            menor= preco
            nomebarato= nomeprod

    cont += 1
    pergunta= str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

    if pergunta != 'S':
        break

print(f'O total gasto na compra foi de R${soma}')
print(f'{maismil} produtos custam mais de R$1.000,00.')
print(f'O nome do produto mais barato é: {nomebarato}')