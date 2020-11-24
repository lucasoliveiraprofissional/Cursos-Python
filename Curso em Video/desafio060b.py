'''Faça um programa que leia um número qualquer
e mostre o seu fatorial.'''

'''Escolhi deixar o programa dele aqui também pois
a lógica que ele fez foi muito boa. Ele usou o if
para dar print em = se estivermos lidando com o 
último elemento fatorial, e fez um if dentro de um
print.'''

n= int(input('Digite um número para calcular seu fatorial: '))
c= n
f= 1

while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))

