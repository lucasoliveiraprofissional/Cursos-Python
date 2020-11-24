#programa que le os catetos de um triangulo retangulo e informe a hipotenusa
from math import hypot

co= float(input('Digite o comprimento do cateto oposto: '))
ca= float(input('Digite o comprimento do cateto adjacente: '))

hipotenusa= hypot(co,ca)

print('A hipotenusa é: {:.2f}'.format(hipotenusa))