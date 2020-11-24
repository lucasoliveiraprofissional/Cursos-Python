'''Faça um programa que leia 5 valores
numericos e guarde-os em uma lista.

No final, mostre qual foi o maior e o
menor valor digitado e as suas respec-
tivas posições na lista.'''


'''Vendo o Guanabara mostrar como ele quer que funcione o programa,
eu conclui que o meu programa não pega todas as possibilidades,
uma vez que podem ter valores menores iguais e valores maiores iguais
também, por isso eu tenho que mostrar todas as posições dos valores
menores e todas as posições dos valores menores. Ex.:
caso o usuário digite 1 e depois 1 e o maior valor for 5 e depois 5
teremos 2 valores menores e 2 maiores.'''

mai= men= 0
numeros= []
for cont in range(0, 5):
    numeros.append(int(input(f'Digite um valor para a posição {cont}: ')))

    if cont == 0:
        mai= men= numeros[cont]

    else:
        if numeros[cont] > mai:
            mai= numeros[cont]
        if numeros[cont] < men:
            men= numeros[cont]

print(f'\nVocê digitou os valores: {numeros}')

print(f'\nO maior valor digitado foi: {mai} nas posições: {}')
for i, v in enumerate(numeros):
    if v == mai:
        print(f'{i}... ', end='')
print()

print(f'\nO menor valor digitado foi: {men} nas posições: {}')
for i, v in enumerate(numeros):
    if v == men:
        print(f'{i}... ', end='')
print()
