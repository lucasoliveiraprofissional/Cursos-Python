'''Crie um programa que vai ler vários
números e colocar em uma lista.

Depois disso, crie duas listas extras
que vão conter apenas os valores pares
e os valores impares digitados,
respectivamente.

Ao final, mostre o conteúdo das três
listas geradas.'''

'''Fiz versão b só para deixar aqui
e por curiosidade do modo que ele usaria.
O meu exercicio funcionou perfeitamente.'''

num= list()
pares= list()
impares= list()

while True:
    num.append(int(input('Digite um numero: ')))
    resp= str(input('Quer continuar? [S/N] '))

    if resp in 'Nn':
        break

for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)

print(f'\nA lista completa é: {num}')
print(f'\nA lista de pares é: {pares}')
print(f'\nA lista de impares é: {impares}')
