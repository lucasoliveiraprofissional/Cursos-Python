'''Desenvolva um programa que leia quatro
valores pelo teclado e guarde-os em uma
tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posicao foi digitado o primeiro
valor 3.
C) Quais foram os números pares.'''

'''Esse programa é direto a versão b pois eu
não tinha ideia de que daria para fazer o que
dá para fazer nesse programa'''

'''Eu imaginei que assim como no exercicio anterior,
fosse preciso também fazer um metodo a cada elemento
do vetor. Assim foi'''

num= (int(input('Digite um numero: ')),
      int(input('Digite um numero: ')),
      int(input('Digite um numero: ')),
      int(input('Digite um numero: ')))

print('')

print(f'Quantas vezes aparece o número 9: {num.count(9)}')

if 3 in num:
    print(f'Em que posição está o número 3: {num.index(3)+1}')
else:
    print('Não existem números 3.')

print(f'Os números pares foram: ', end='')

for n in num:
    if n % 2 == 0:
        print(n, end=' ')

