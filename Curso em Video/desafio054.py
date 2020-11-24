'''Crie um programa que leia o ano de nascimento
de sete pessoas. No final, mostre quantas
pessoas ainda não atingiram a maioridade e quantas
já são maiores'''

'''Por melhoria no código, importei o modulo que pega a data'''
from datetime import date

atual= date.today().year
menores= 0
maiores= 0

for c in range(0, 8):
    idade= int(input('Digite o ano de nascimento: '))

    if atual - idade < 18:
        menores+= 1
    else:
        maiores+= 1

print('')
print('{} Pessoas não atingiram a maioridade e {} atingiram.'.format(menores, maiores))

