'''Desenvolva um programa que leia seis números inteiros
e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for impar, desconsidere-o.'''

soma= 0
for laco in range(0, 6):
    num= int(input('Digite um numero inteiro: '))

    if num % 2 == 0:
        soma += num

print('')
print('Soma dos pares: {}'.format(soma))