'''Faça um programa que leia 5 valores
numericos e guarde-os em uma lista.

No final, mostre qual foi o maior e o
menor valor digitado e as suas respec-
tivas posições na lista.'''

numeros= []
for cont in range(0, 5):
    numeros.append(int(input('Digite um valor: ')))

print(f'\nVoce digitou os valores: {numeros}', end='')

print(f'\nO menor valor é {min(numeros)} e sua posição é {numeros.index(min(numeros))+1}')
print(f'O maior valor é {max(numeros)} e sua posição é {numeros.index(max(numeros))+1}')

'''Vendo o Guanabara mostrar como ele quer que funcione o programa,
eu conclui que o meu programa não pega todas as possibilidades,
uma vez que podem ter valores menores iguais e valores maiores iguais
também, por isso eu tenho que mostrar todas as posições dos valores
menores e todas as posições dos valores menores. Ex.:
caso o usuário digite 1 e depois 1 e o maior valor for 5 e depois 5
teremos 2 valores menores e 2 maiores.'''