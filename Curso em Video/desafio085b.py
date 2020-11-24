'''Crie um programa onde o usuário
possa digitar sete valores numéricos
e acadastre-os em uma lista única que
mantenha separados os valores pares e
impares. No final, mostre os valores
pares e impares em ordem crescente.
Ele quer que ordene a lista dos
pares e a lista dos ímpares, é fácil
também.'''

'''Trabalharemos com lista dentro de lista.'''

'''Já conseguimos na declaração colocar uma lista dentro de outra'''
num= [[], []]
valor= 0

for c in range(1, 8):
    valor= int(input(f'Digite o {c}º valor: '))

    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

print(f'\nTodos os valores: {num}')

num[0].sort()
num[1].sort()

print(f'Os valores pares digitados foram {num[0]}')
print(f'Os valores ímpares digitados foram {num[1]}')