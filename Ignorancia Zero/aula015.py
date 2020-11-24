'''Dizemos que um número natural é triangular se ele é produto
de três números naturais consecutivos.

Ex.: 120 é triangular, pois 4.5.6 == 120.

Dado um inteiro não-negativo n, verificar se n é triangular.'''

#40 por ex é triangular?
#a menor possibilidade que temos é:
#1x2x3 == 6, precisamos ir testando 1 a 1 até
#chegar ao número desejado.

#2x3x4 == 24
#3x4x5 == 60

num= int(input('Digite um numero inteiro não negativo: '))

i= 1

while i * (i + 1) * (i + 2) < num:
    i+= 1

if i * (i + 1) * (i + 2) == num:
    print('{} é triangular'.format(num))
else:
    print('{} não é triangular'.format(num))


