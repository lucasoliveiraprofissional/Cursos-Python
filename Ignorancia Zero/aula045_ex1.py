'''Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
Ex.: 5!= 5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:

Fatorial de: 5
5! = 5. 4. 3. 2. 1 = 120. '''

n= int(input('Fatorial de: '))
acum=0

print(f'{n}! =', end='')

i=n

for i in (n, 2):
    acum *= i
    print(f'{acum}')
'''
    if i == 2:
        print(f' 1 = ')
    else:
        print(f' {i}', end=' .')

print(f'{acum}')
'''