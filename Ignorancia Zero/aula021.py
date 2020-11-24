'''Inteiros interagindo com Reais'''
'''Faça um programa que peça 2 numeros inteiros e 1 numero real
Calcule e mostre:
a. O produto do dobro do primeiro com metade do segundo.
b. a soma do triplo do primeiro com o terceiro.
c. o terceiro elevado ao cubo.'''

int1= int(input('Digite o primeiro numero (inteiro): '))
int2= int(input('Digite o segundo numero (inteiro): '))
real= int(input('Digite o terceiro numero (real): '))

print((2*int1)*(int2/2))
print(3*int1 + real)
print(real**3)

#(o resultado será sempre exibido como real, ou seja, numero.0)