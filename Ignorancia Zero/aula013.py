'''Fazer a exponenciação sem utilizar o **'''


base= int(input('Digite a base: '))
exp= int(input('Digite o expoente: '))

n = 0
produto = 1

while n < exp:
    produto = produto * base
    n = n + 1

print('Resultado: {}'.format(produto))

