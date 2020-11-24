'''Nesse caso, ele le o flag do lado de fora e de dentro.'''

num= 0
soma= 0

num= int(input('Digite um número inteiro: '))

while num != 999:
    if num != 999:
        num= int(input('Digite um número inteiro: '))
        soma+= num

print('A soma dos números digitados é: {}'.format(soma))
