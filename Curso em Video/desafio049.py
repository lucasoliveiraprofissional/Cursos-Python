'''Refaça o desafio 009, mostrando a tabuada
de um número que o usuário escolher, só que
agora utilizando um laço for.'''

numero= int(input('Digite um número para saber sua tabuada: '))
print('')

for multiplicador in range(0, 11):
    print('{} X {} = {}'.format(numero, multiplicador, numero * multiplicador))